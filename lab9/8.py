# 8) WAP that defines a function that returns one if the number is prime otherwise returns zero.

def fprime(n):
    flag = 1
    for i in range(2, n):
        if(n%i == 0):
            flag = 0
            break
        else:
            flag = 1
    return flag

n = int(input("Enter n:"))

print(fprime(n))
