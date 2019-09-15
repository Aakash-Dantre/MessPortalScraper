from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

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
arr=['','breakfast[]','lunch[]','dinner[]']


driver = webdriver.Chrome(chrome_options=opts)
driver.get('https://mess.iiit.ac.in')
sleep(1)
username_box=driver.find_element_by_id('username')
username_box.send_keys('aakash.dantre@students.iiit.ac.in')

password_box=driver.find_element_by_id('password')
password_box.send_keys('Mayor.1mdb')

driver.find_element_by_class_name('btn-submit').click()

driver.get('https://mess.iiit.ac.in/mess/web/student_cancel.php')

print(color.BOLD+color.CYAN+'TODAY OR TOMMOROW'.center(40,"*")+color.END)
print(color.BLUE+"1:today"+color.END)
print(color.BLUE+"2:tommorow"+color.END)
f=int(input())

print(color.BOLD+color.CYAN+"ENTER MEAL TO CANCEL".center(40,"*")+color.END)
print(color.BLUE+"1:Breakfast"+color.END)
print(color.BLUE+"2:Lunch"+color.END)
print(color.BLUE+"3:Dinner"+color.END)
n=int(input())
meal=arr[n]

if f == 2:
	end=driver.find_element_by_xpath("//input[@name='enddate']")
	date=end.get_attribute("value")
	dated=date[0:2]
	dated=int(dated)+1
	final=str(dated)+date[2:]
	scr1="document.getElementsByName(\"enddate\")[0].setAttribute(\"value\",\""+final+"\")"
	scr2="document.getElementsByName(\"startdate\")[0].setAttribute(\"value\",\""+final+"\")"
	driver.execute_script(scr1)
	driver.execute_script(scr2)

driver.find_element_by_xpath("//input[@name='"+meal+"']").click()

driver.find_element_by_xpath("//*[@id=\"content\"]/div[2]/form/div/input").click()

resp=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/font").text

if resp=="Invalid Date":print(color.BOLD+color.RED+"INVALID DATE".center(40,"*")+color.END)
else:print(color.BOLD+color.GREEN+"ALL CHANGES ARE MADE SUCCESSFULLY".center(40,"*")+color.END+color.END)
