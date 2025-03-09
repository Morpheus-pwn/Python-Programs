# Program to find the sum of all even numbers in a group of n numbers entered by the user.

n = int(input("Enter the number of elements: "))
sum = 0
for i in range(1, n+1):
    num = int(input(f"Enter element {i}: "))
    if num % 2 == 0:
        sum += num
print(f"The sum of all even numbers is: {sum}")
