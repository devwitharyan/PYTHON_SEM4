# WAP to create calculator module that defines functions like addition, substractuib, multiplication and division, user calculator module in another file.

import calc_mod as calc

a = int(input("Enter A: "))
b = int(input("Enter B: "))

print("Addition:", calc.add(a,b))
print("Substraction:", calc.sub(a,b))
print("Multiplication:", calc.mul(a,b))
print("Division:", calc.div(a,b))
