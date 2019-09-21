from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import inquirer

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


opts = Options()
opts.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=opts)
driver.get('https://mess.iiit.ac.in')
sleep(1)
username_box=driver.find_element_by_id('username')
username_box.send_keys('user')

password_box=driver.find_element_by_id('password')
password_box.send_keys('pass')

driver.find_element_by_class_name('btn-submit').click()

driver.get('https://mess.iiit.ac.in/mess/web/student_cancel.php')

date=[
	inquirer.List('dates',message=color.BOLD+color.CYAN+'TODAY OR TOMMOROW'.center(40,"*")+color.END,choices=['TODAY','TOMMOROW'],),
]
dat=inquirer.prompt(date)
f=dat.get('dates')

meals = [
  inquirer.Checkbox('interests',
                    message=color.BOLD+color.CYAN+"SELECT MEALS".center(40,"*")+color.END+"---using space",
                    choices=['breakfast','lunch','dinner','uncancel'],
                    ),
]
check = inquirer.prompt(meals)

meals=check.get('interests')
uncancel=0
if 'uncancel' in meals:
	uncancel=1 
	meals.remove('uncancel')

for meal in meals:
	if f == 'TOMMOROW':
		end=driver.find_element_by_xpath("//input[@name='enddate']")
		date=end.get_attribute("value")
		dated=date[0:2]
		dated=int(dated)+1
		final=str(dated)+date[2:]
		scr1="document.getElementsByName(\"enddate\")[0].setAttribute(\"value\",\""+final+"\")"
		scr2="document.getElementsByName(\"startdate\")[0].setAttribute(\"value\",\""+final+"\")"
		driver.execute_script(scr1)
		driver.execute_script(scr2)

	driver.find_element_by_xpath("//input[@name='"+meal+"[]']").click()

	if uncancel:driver.find_element_by_xpath("//input[@name='uncancel[]']").click()

	driver.find_element_by_xpath("//*[@id=\"content\"]/div[2]/form/div/input").click()

	resp=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/font").text

	if resp=="Invalid Date":print("    "+color.BOLD+color.RED+"INVALID DATE".center(40,"*")+color.END)
	else:print("    "+color.BOLD+color.GREEN+"CHANGE IS MADE SUCCESSFULLY".center(40,"*")+color.END+color.END)
	print("    ")

driver.close()