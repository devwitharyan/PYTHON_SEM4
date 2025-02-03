# 6) WAP to to generate fibonacci series using function.

def fibo(n):
    a = 0
    b = 1
    temp = 0
    for i in range(n):
        print(temp)
        a = b
        b = temp
        temp = a + b
        
n = int(input("Enter n: "))
fibo(n)
