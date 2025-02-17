#WAP to find longest word in firstfile.txt

file = open("firstfile.txt", 'r')
filelst = file.readlines()
long = ""
for i in filelst:
    for j in i.split():
        if len(j) > len(long):
            long = j
print("Longest word is: ", long)
file.close()
