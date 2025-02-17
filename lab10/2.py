#WAP to read the first 5 lines from the file firstfile.txt

with open("./firstfile.txt", 'r') as file:
    for i in range(0,5):
        print(file.readline())