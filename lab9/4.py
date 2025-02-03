# 4) WAP to take a string from user and pass it as an argument and convert all lower case characters into uppercase using function.

def low2up(str):
    return str.upper()
str = input("Enter string: ")
print(low2up(str))

def low2up(s):
    return ''.join(c.upper() if c.islower() else c for c in s)

s = input("Enter string: ")
print(low2up(s))
