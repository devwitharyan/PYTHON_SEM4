# WAP to print persons age in years and also print how many days remaining for their next birthday

import datetime

date = input("Enter date as yyyy-mm-dd : ")
date = datetime.datetime.strptime(date,"%Y-%m-%d")

y = date.year
m = date.month
d = date.day

today = datetime.date.today()
date = datetime.date(y,m,d)
day = today - date
print("age is :" ,(day.days)/365)

date = date.replace(year= 2025)
remain = date-today
if remain.days < 0 :
    date = date.replace(year= 2026)
    remain = date-today

print("remaing day for next birthday is : ", remain)
