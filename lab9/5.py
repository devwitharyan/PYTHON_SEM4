# 5) WAP to find factorial of a given number using function.

def facto(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
n = int(input("Enter n: "))
print(facto(n))
     