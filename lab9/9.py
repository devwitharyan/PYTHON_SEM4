# 9) WAP to find factorial of a given number using recursion.

def fact(n):
    if(n == 0):
        return 1
    elif(n == 1):
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter n"))
print(fact(n))