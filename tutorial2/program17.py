# Write a Python program to print the factorial of a number using recursion.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
result = factorial(n)
print("The factorial of", n, "is", result)
