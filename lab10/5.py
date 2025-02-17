#WAP to read a file line by line and store it as a list

with open("./firstfile.txt", 'r') as file:
    filelst = file.readlines()
    print(filelst)
