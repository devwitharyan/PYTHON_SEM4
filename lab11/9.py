# WAP to find day of the week of a given date

from datetime import datetime

date = input("Enter a date (yyyy-mm-dd): ")
date_for = datetime.strptime(date, "%Y-%m-%d")
print(date_for.weekday())
print("Day of the week:", date_for.strftime("%A"))
