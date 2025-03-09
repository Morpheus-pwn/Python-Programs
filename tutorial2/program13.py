# Write a python function to find the area of a circle.

import math
def find_circle_area(radius):
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))
area = find_circle_area(radius)
print("The area of the circle is:", area)