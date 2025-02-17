# WAP to read only special characters from file

file = open("firstfile.txt", 'r')
for i in file.read():
    if not i.isalnum():
        print(i, end="")
file.close()