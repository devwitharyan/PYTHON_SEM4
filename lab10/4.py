#WAP to write n lines in new file.

file1 = open("secondfile.txt", 'w')
n = int(input("Enter number of lines: "))
for i in range(n):
    file1.write(input() + "\n")
file1.close()
