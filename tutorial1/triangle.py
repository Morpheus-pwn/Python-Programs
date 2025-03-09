b=int(input("enter the first side of the triangle:"))
h=int(input("enter the second side of the triangle:"))
hy=int(input("enter the third side of the triangle:"))

if hy**2==b**2+h**2:
    print("it is a right angle triangle")
else:
    print("it is not a right angle triangle")
