# WAP to sort a dictionary by key in ascending and descending order

n = int(input("Enter size : "))
dict = {}

for i in range(n):
    key = int(input("Enter key : "))
    val = int(input("Enter value : "))
    dict[key] = val

keys = list(dict.keys())
keys.sort()
acen = {}
desen ={}
for i in keys:
    acen[i] = dict[i]

keys.sort(reverse=True)
for i in keys:
    desen[i] = dict[i]

print(acen,desen)