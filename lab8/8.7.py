# WAP to merge two dictionary given by the user into one dictionary

n1 = int(input("Enter size for dictionary 1 : "))
n2 = int(input("Enter size for dictionary 2 : "))

dict1 = {}
dict2 = {}

print("Enter key value pair for dictionary 1 : ")
for i in range(n1):
    key = input("Enter key : ")
    val = input("Enter value : ")
    dict1[key] = val

print("Enter key value pair for dictionary 2 : ")
for i in range(n2):
    key = input("Enter key : ")
    val = input("Enter value : ")
    dict2[key] = val

dict3 = dict1 | dict2
print(dict3)