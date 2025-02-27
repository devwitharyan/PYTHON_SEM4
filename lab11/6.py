# WAP to pick random element from given list
import random

n = int(input("Enter size of list: "))

l = []

for i in range(n):
    l.append(int(input("Enter element: ")))

print("Random element: ", random.choice(l))