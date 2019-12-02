from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import inquirer
from datetime import date
from datetime import timedelta

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

dayes=['MONDAY\'S','TUESDAY\'S','WEDNESDAY\'S','THURSDAY\'S','FRIDAY\'S','SATURDAY\'S','SUNDAY\'S']

opts = Options()
opts.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=opts)
driver.get('https://mess.iiit.ac.in')
sleep(1)
username_box=driver.find_element_by_id('username')
username_box.send_keys('USER')

password_box=driver.find_element_by_id('password')
password_box.send_keys('PASS')

driver.find_element_by_class_name('btn-submit').click()

driver.get('https://mess.iiit.ac.in/mess/web/student_cancel.php')

today=date.today()
datelist=['TODAY']
for i in range(1,8):
	date=today+timedelta(days=i)
	datelist.append(str(date))
datelist+=dayes
date=[
	inquirer.Checkbox('dates',message=color.BOLD+color.CYAN+'SELECT THE DATE'.center(40,"*")+color.END,choices=datelist,),
]
dat=inquirer.prompt(date)
alldates=dat.get('dates')


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

if 'TODAY' in alldates:
	alldates.append(str(today))

for i in range(7):
	if dayes[i] in alldates:
		da=today
		while da.weekday()!=i:
			da+=timedelta(days=i)
		for i in range(4):
			alldates.append(str(da+timedelta(days=(i*7))))

alldates = [i for i in alldates if "DAY" not in i]

for f in alldates:
	try:
		end=driver.find_element_by_xpath("//input[@name='enddate']")
	except:
		print(color.RED+color.BOLD+"WRONG PASSWORD OR NO ACCESS TO IIIT NETWORK"+color.END)
		exit()
	scr1="document.getElementsByName(\"enddate\")[0].setAttribute(\"value\",\""+f+"\")"
	scr2="document.getElementsByName(\"startdate\")[0].setAttribute(\"value\",\""+f+"\")"
	driver.execute_script(scr1)
	driver.execute_script(scr2)

	for meal in meals:
		driver.find_element_by_xpath("//input[@name='"+meal+"[]']").click()


	if uncancel:driver.find_element_by_xpath("//input[@name='uncancel[]']").click()

	driver.find_element_by_xpath("//*[@id=\"content\"]/div[2]/form/div/input").click()

	resp=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/font").text

	if resp=="Invalid Date":
		res="INVALID DATE for "+f
		print("    "+color.BOLD+color.RED+str(res).center(40,"*")+color.END)
	else:
		res="CHANGE IS MADE SUCCESSFULLY for "+f
		print("    "+color.BOLD+color.GREEN+str(res).center(40,"*")+color.END+color.END)
	print("    ")

driver.close()