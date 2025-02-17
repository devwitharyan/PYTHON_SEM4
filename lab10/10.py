#WAP to enter a file name and check if it exist of not ask for user conformation and delete the file
import os
file = open(input("Enter file name: "), 'r')
print("File exist")
if input("Do you want to delete the file?: ") == 'y'.lower():
    file.close()
    os.remove(file.name)
    print("File deleted")
