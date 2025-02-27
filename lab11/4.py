# WAP to demonstrate datetime module

import datetime

date = input("Enter date as dd-mm-yyyy : ")
date = datetime.datetime.strptime(date,"%d-%m-%Y")
print("date : ", date)

print("formated date : ", date.strftime("%d,%b,%Y  %H::%M::%S"))
print("weekday [0-6] : ", date.weekday())
print("weekday [1-7] : ", date.isoweekday())
print("new dateime : ", date.replace(hour = 4 , minute = 25 , second = 45, microsecond = 43631))
print("only date : ", date.date())
print("date : ", date.day)
print("month : ", date.month)
print("year : ", date.year)