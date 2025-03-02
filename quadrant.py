x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
  quadrant = 1
elif x < 0 and y > 0:
  quadrant = 2
elif x < 0 and y < 0:
  quadrant = 3
elif x > 0 and y < 0:
  quadrant = 4
else:
  quadrant = "Origin"

print("The point lies in Quadrant", quadrant)
