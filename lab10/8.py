#WAP to find the size of file

file = open("firstfile.txt", 'r')
# file.read()
file.seek(0,2)
print(file.tell())
file.close()