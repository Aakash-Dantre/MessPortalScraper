from selenium import webdriver
from time import sleep
import datetime
import csv
from selenium.webdriver.chrome.options import Options
#from selenuim.webdriver.chrome.options import Options
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

# opts.set_headless()
# assert opts.headless  # Operating in headless mode

driver = webdriver.Chrome(chrome_options=opts)
driver.get('https://mess.iiit.ac.in')
sleep(1)
username_box=driver.find_element_by_id('username')
username_box.send_keys('aakash.dantre@students.iiit.ac.in')

password_box=driver.find_element_by_id('password')
password_box.send_keys('Mayor.1mdb')

driver.find_element_by_class_name('btn-submit').click()


results = driver.find_elements_by_class_name("post")

data=results[1].text

# print(data)

lst=[]
lst=data.split("\n")

b=1;l=1;d=1
breakfast=lst[3][10:]+".csv"
lunch=lst[4][6:]+".csv"
dinner=lst[5][7:]+".csv"
if(breakfast=="Cancelled.csv"):b=0
if(lunch=="Cancelled.csv"):l=0
if(dinner=="Cancelled.csv"):d=0

x=datetime.datetime.now()
day=int(x.strftime("%w"))
if day == 0:
	day=7
day+=1

print(color.BOLD+color.BLUE+"Breakfast menu".center(40,"*")+color.END)
if b==1:
	print (color.BOLD+color.CYAN+breakfast[0:-4].center(20,"-")+color.END)
	with open(breakfast,'rt') as csvfile:
		data=csv.reader(csvfile)
		i=0
		for row in data:
			i+=1
			if i>=4 :
				if not row[day]:continue
				print(color.BOLD+color.GREEN+row[day]+color.END)
			if i>=11: break
else:print(color.BOLD+color.RED+"Cancelled"+color.END)

print(color.BOLD+color.BLUE+"\n\n"+"Lunch menu".center(40,"*")+color.END)
if l==1:
	print (color.BOLD+color.CYAN+lunch[0:-4].center(20,"-")+color.END)
	with open(lunch,'rt') as csvfile:
		data=csv.reader(csvfile)
		i=0
		for row in data:
			i=i+1
			if i>=13 :
				if not row[day]:continue
				print(color.BOLD+color.GREEN+row[day]+color.END)
			if i>=23: break
else:print(color.BOLD+color.RED+"Cancelled"+color.END)

print(color.BOLD+color.BLUE+"\n\n"+"Dinner menu".center(40,"*")+color.END)
if d==1:
	print (color.BOLD+color.CYAN+dinner[0:-4].center(20,"-")+color.END)
	with open(dinner,'rt') as csvfile:
		data=csv.reader(csvfile)
		i=0
		for row in data:
			i=i+1
			if i>=27 :
				if not row[day]:continue
				print(color.BOLD+color.GREEN+row[day]+color.END)
			if i>44: break	
else:print(color.BOLD+color.RED+"Cancelled"+color.END)

driver.close()
