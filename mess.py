from selenium import webdriver
from time import sleep
import csv
import datetime
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

x=datetime.datetime.now()
day=int(x.strftime("%w"))
if day == 0:
	day=7
day+=1

type1=[4,13,27]
type2=[11,23,42]
def function(messname,t,n):
	print (color.BOLD+color.CYAN+messname.center(20,"-")+color.END)
	if(n==1):return
	with open("mess/"+messname+".csv",'rt') as csvfile:
		data=csv.reader(csvfile)
		i=0
		for row in data:
			i=i+1
			if i>=type1[t] :
				if not row[day]:continue
				print(color.BOLD+color.GREEN+row[day]+color.END)
			if i>type2[t]: break	
if __name__=="__main__":
	opts = Options()
	opts.set_headless(headless=True)
	driver = webdriver.Chrome(chrome_options=opts)
	driver.get('https://mess.iiit.ac.in')
	sleep(1)
	try:	username_box=driver.find_element_by_id('username')
	except: 
		print(color.BOLD+color.RED+"error getting the connection(open vpn)"+color.END)
		exit(1)
	username_box.send_keys('USER')
	password_box=driver.find_element_by_id('password')
	password_box.send_keys('PASS')
	driver.find_element_by_class_name('btn-submit').click()
	results = driver.find_elements_by_class_name("post")
	data=results[1].text
	lst=[]
	lst=data.split("\n")
	b=1;l=1;d=1;nb=0;nl=0;nd=0;
	breakfast=lst[3][10:]+".csv"
	lunch=lst[4][6:]+".csv"
	dinner=lst[5][7:]+".csv"
	if(breakfast=="Cancelled.csv"):b=0
	if(lunch=="Cancelled.csv"):l=0
	if(dinner=="Cancelled.csv"):d=0
	if(breakfast=="Kadamb Non-Veg.csv"):nb=1
	if(lunch=="Kadamb Non-Veg.csv"):nl=1
	if(dinner=="Kadamb Non-Veg.csv"):nd=1
	print(color.BOLD+color.BLUE+"Breakfast menu".center(40,"*")+color.END)
	if b==1:
		function(breakfast[0:-4],0,nb)
	else:print(color.BOLD+color.RED+"Cancelled"+color.END)

	print(color.BOLD+color.BLUE+"\n\n"+"Lunch menu".center(40,"*")+color.END)
	if l==1:
		function(lunch[0:-4],1,nl)
	else:print(color.BOLD+color.RED+"Cancelled"+color.END)

	print(color.BOLD+color.BLUE+"\n\n"+"Dinner menu".center(40,"*")+color.END)
	if d==1:
		function(dinner[0:-4],2,nd)
	else:print(color.BOLD+color.RED+"Cancelled"+color.END)
	driver.close()

