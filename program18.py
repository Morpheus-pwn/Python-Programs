# Write a Python program to print n’th Fibonacci number using recursion.

def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter the value of n: "))
if n <= 0:
    print("Incorrect input")
else:
    print(f"The {n}th Fibonacci number is {fibonacci(n)}")
    
print("The Fibonacci sequence is:")
for i in range(1, n+1):
    print(fibonacci(i))
    

    