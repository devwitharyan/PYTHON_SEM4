# 2) WAP That defines a function to add first n numbers.

def addn(n):
    sumn = 0
    for i in range(n+1):
        sumn = sumn + i
    return sumn
    
n = int(input("Enter n: "))

print(addn(n))