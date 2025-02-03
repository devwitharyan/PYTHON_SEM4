# WAPTo convert given set into tuple and list 

n = int(input("Enter the number of elements: "))
s = set()
for i in range(n):
    s.add(int(input()))
print(s)

t = tuple(s)
l = list(s)
print("Tuple:", t)
print("List:", l)