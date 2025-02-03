# WAP to sort a dictionary by value in ascending and descending order

n = int(input("Enter size : "))
dict = {}

for i in range(n):
    key = input("Enter key : ")
    val = int(input("Enter value : "))
    dict[key] = val

val = list(dict.values())
val.sort()
acen = {}
desen ={}

for i in val:
    for j in dict:
        if dict[j] == i:
            acen[j] = dict[j]
print(acen)

val.sort(reverse=True)
for i in val:
    for j in dict:
        if dict[j] == i:
            desen[j] = dict[j]
print(desen)