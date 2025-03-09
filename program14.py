# Write a python program to compute nCr using a factorial function.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
nCr = factorial(n) // (factorial(r) * factorial(n-r))
print("The value of nCr is:", nCr)