# WAP to convert two list into a dictionary

n = int(input("Enter size of dictionary: "))

keys = []
values = []

print("Enter keys:")
for i in range(n):
    keys.append(input())

print("Enter values:")
for i in range(n):
    values.append(input())

dictionary = {}

for i in range(n):
    dictionary[keys[i]] = values[i]

print("Dictionary:", dictionary)