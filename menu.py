import datetime
import csv
import inquirer

x=datetime.datetime.now()
today=int(x.strftime("%w"))
if today == 0:
	today=7
today-=1
class color:
   PURPLE = '\033[95m'
   BLUE = '\033[96m'
   DARKCYAN = '\033[36m'
   CYAN = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
days=["1.MONDAY","2.TUESDAY","3.WEDNESDAY","4.THURSDAY","5.FRIDAY","6.SATURDAY","7.SUNDAY"]
days[today]=days[today][0:2]+color.RED+days[today][2:]
da = [
    inquirer.List('d',
                  message=color.BOLD+color.GREEN+"SELECT THE DAY".center(40,"*"),
                  choices=days,
              ),
]
day=inquirer.prompt(da)
day=day.get('d')
print("    "+day[0])
day=int(day[0])
day+=1

messes=['Yuktahaar','south','north','Kadamb-Veg']
questions = [
    inquirer.List('mess',
                  message=color.BOLD+color.GREEN+"SELECT YOUR MESS".center(40,"*"),
                  choices=messes,
              ),
]

answers = inquirer.prompt(questions)
messp = answers.get('mess')
mess=messp+".csv"

meals = [
  inquirer.Checkbox('interests',
                    message=color.BOLD+color.GREEN+"SELECT MEALS form spacebar".center(40,"*"),
                    choices=['Breakfast','Lunch','Dinner'],
                    ),
]
check = inquirer.prompt(meals)

meal=check.get('interests')
	
if 'Breakfast' in meal:
	print("    "+color.BOLD+color.BLUE+"Breakfast menu".center(40,"*")+color.END)
	print("    "+color.BOLD+color.CYAN+messp.center(20,"-")+color.END)
	with open(mess,'rt') as csvfile:
		data=csv.reader(csvfile)
		i=0
		for row in data:
			i+=1
			if i>=4 :
				if not row[day]:continue
				print("    "+color.BOLD+color.GREEN+row[day]+color.END)
			if i>=11: break
	print("    "+"\n\n")											

if 'Lunch' in meal:
	print("    "+color.BOLD+color.BLUE+"Lunch menu".center(40,"*")+color.END)
	print("    "+color.BOLD+color.CYAN+messp.center(20,"-")+color.END)
	with open(mess,'rt') as csvfile:
		data=csv.reader(csvfile)
		i=0
		for row in data:
			i+=1
			if i>=13 :
				if not row[day]:continue
				print("    "+color.BOLD+color.GREEN+row[day]+color.END)
			if i>=23: break
	print("    "+"\n\n")											

if 'Dinner' in meal:
	print("    "+color.BOLD+color.BLUE+"Dinner menu".center(40,"*")+color.END)
	print("    "+color.BOLD+color.CYAN+messp.center(20,"-")+color.END)
	with open(mess,'rt') as csvfile:
		data=csv.reader(csvfile)
		i=0
		for row in data:
			i+=1
			if i>=27 :
				if not row[day]:continue
				print("    "+color.BOLD+color.GREEN+row[day]+color.END)
			if i>=44: break
	print("    "+"\n\n")											

