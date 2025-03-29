# Write a Python program to find the quadrant of a point, say (x,y).

def find_quadrant(x, y):
  if x > 0 and y > 0:
    return 1
  elif x < 0 and y > 0:
    return 2
  elif x < 0 and y < 0:
    return 3
  elif x > 0 and y < 0:
    return 4
  else:
    return 0

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

quadrant = find_quadrant(x, y)

if quadrant == 0:
  print("The point lies on an axis.")
else:
  print(f"The point ({x}, {y}) lies in Quadrant {quadrant}.")