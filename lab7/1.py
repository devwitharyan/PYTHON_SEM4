# WAP to create a set using the list of elements entered by user

n = int(input("Enter the number of elements: "))
l = []
for i in range(n):
    l.append(int(input()))
s = set(l)
print(s)

