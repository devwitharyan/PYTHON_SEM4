# WAP to enter a key and remove a key from dictionary if it exists

n = int(input("Enter size : "))
dict = {}

for i in range(n):
    key = input("Enter key : ")
    val = input("Enter value : ")
    dict[key] = val

key = input("Enter key : ")

if key in dict :
    dict.pop(key)

print(dict)