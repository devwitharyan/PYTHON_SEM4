# WAP to create a dictionary from a string

str = input("Enter string : ")
dict = {}

for i in range(len(str)):
    dict[i] = str[i]

print(dict)