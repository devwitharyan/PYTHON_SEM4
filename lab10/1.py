#WAP to read the file named firstfile.txt

with open("./firstfile.txt", 'r') as file:
    print(file.read())