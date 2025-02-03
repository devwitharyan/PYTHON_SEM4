# WAP to perform union, intersection, difference and symmetric difference of two sets

n = int(input("Enter the number of elements in set 1: "))
s1 = set()
for i in range(n):
    s1.add(int(input()))
print(s1)

n2 = int(input("Enter the number of elements in set 2: "))
s2 = set()
for i in range(n2):
    s2.add(int(input()))
print(s2)


print("Union:", s1.union(s2))
print("Intersection:", s1 & s2)
print("Difference:", s1 - s2)
print("Symetric difference:", s1 ^ s2)