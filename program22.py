# Program to read list of numbers and find the median

numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
numbers.sort()

n = len(numbers)
if n % 2 == 0:
    median = (numbers[n//2] + numbers[n//2 - 1]) / 2
else:
    median = numbers[n//2]

print("The median of the list is:", median)