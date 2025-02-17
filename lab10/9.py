#WAP to append content of studentdetails.txt file by reading student records from user

file = open("./stddet.txt", 'a')
n = input("Enter number of student to append: ")
for i in range(n):
    file.write("rollno: " + input("Enter rollno: ") + "\n")
    file.write("Name: " + input("Enter Name: ") + "\n")
    file.write("Dep: " + input("Enter Department: ") + "\n" + ".............................." + "\n")
file.close()
