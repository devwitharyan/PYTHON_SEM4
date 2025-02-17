# WAP to write 5 student records (rollno, name, department) to the studentdetails.txt

file = open("./stddet.txt", 'w')
for i in range(2):
    file.write("rollno: " + input("Enter rollno: ") + "\n")
    file.write("Name: " + input("Enter Name: ") + "\n")
    file.write("Dep: " + input("Enter Department: ") + "\n" + ".............................." + "\n")
file.close()

    
    