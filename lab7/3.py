# WAP to remove elemets from set

n = int(input("Enter the number of elements: "))
s = set()
for i in range(n):
    s.add(int(input()))
print(s)

n = int(input("Enter the number to remove: "))
s.remove(n)
print(s)