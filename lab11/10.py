# WAP to print persons age in years and also print how many days remaining for their next birthday

import datetime

y = int(input("Enter year : "))
m = int(input("Enter month : "))
d = int(input("Enter day : "))

today = datetime.date.today()
date = datetime.date(y,m,d)
day = today - date
print("age is :" ,(day.days)/365)

date = date.replace(year= 2025)
print("remaing day for next birthday is : ", date-today)
