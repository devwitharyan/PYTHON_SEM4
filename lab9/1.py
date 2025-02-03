# 1) WAP to calc SI using function.

def si(p,r,t):
    return (p*r*t)/100

p = int(input("Enter P"))
r = int(input("Enter r"))
t = int(input("Enter t"))
print(si(p,r,t))