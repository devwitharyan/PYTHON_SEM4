# wap to find minimum and maximum value from set

n = int(input("Enter the number of elements: "))
s = set()
for i in range(n):
    s.add(int(input()))
print(s)

print("Minimum value in set is", min(s))
print("Maximum value in set is", max(s))