# WAP to create a dictionary for n values and print size of the dictionary

n = int(input("Enter size : "))
dict = {}

for i in range(n):
    key = input("Enter key : ")
    val = input("Enter value : ")
    dict[key] = val 

print(dict,n)
