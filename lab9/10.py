# 10) WAP to generate fibonacci series of n numbers using recursion.

def fiborec(n):
    if(n==0 or n==1):
        return n
    else:
        return (fiborec(n-1)+fiborec(n-2))

n = int(input("Enter n: "))
for i in range(n):
    print(fiborec(i))
    i +=1