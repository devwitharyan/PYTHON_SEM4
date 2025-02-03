# WAP to enter key and add key to a dictionary if it does not exist

n = int(input("Enter size : "))
dict = {}

for i in range(n):
    key = input("Enter key : ")
    val = input("Enter value : ")
    dict[key] = val

key = input("Enter key : ")

if key not in dict :
    val = input("Enter val : ")
    dict[key] = val

print(dict)