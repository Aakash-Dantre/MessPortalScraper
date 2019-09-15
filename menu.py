import datetime
import csv

x=datetime.datetime.now()
day=int(x.strftime("%w"))
if day == 0:
	day=7
day+=1

print("ENTER MESS")
print("1:Yukthar")
print("2:South")
print("3:North")
print("4:Kadamb")

m = int(input())
allmess=['','Yukthaar.csv','south.csv','north.csv','Kadamb-Veg.csv']


if(m==1 or m==2 or m==3 or m==4):

	mess=allmess[m]
	print("ENTER TIME")
	print("1:breakfast")
	print("2:lunch")
	print("3:dinner")
	f=int(input())
	if(f==1):
		with open(mess,'rt') as csvfile:
			data=csv.reader(csvfile)
			i=0
			for row in data:
				i+=1
				if i>=4 :
					if not row[day]:continue
					print(row[day])
				if i>=11: break
	elif(f==2):
		with open(mess,'rt') as csvfile:
			data=csv.reader(csvfile)
			i=0
			for row in data:
				i+=1
				if i>=13 :
					if not row[day]:continue
					print(row[day])
				if i>=23: break
	elif(f==3):
		with open(mess,'rt') as csvfile:
			data=csv.reader(csvfile)
			i=0
			for row in data:
				i+=1
				if i>=27 :
					if not row[day]:continue
					print(row[day])
				if i>=44: break
	else:
		print("invalid")									

else:
	print ("invallid")	