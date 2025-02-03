# 7) WAP to implement a simple calc using lambda function.

calc = lambda a, exp, b: a+b if(exp == "+") else a-b if (exp =="-") else a*b if(exp == "*") else a/b if(exp == "/") else "Enter valid exp"

a = int(input("Enter a:"))
b = int(input("Enter b:"))
exp = input("Enter exp: ")
print("calc", calc(a,exp, b))