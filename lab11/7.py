# WAP to calculat area of circle, triangle, and rectangle using math module without function

import math

r = float(input("Enter radius of circle: "))
print("Area of circle: ", math.pi * r * r)

b = float(input("Enter base of triangle: "))
h = float(input("Enter height of triangle: "))
print("Area of triangle: ", 0.5 * b * h)

l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
print("Area of rectangle: ", l * w)