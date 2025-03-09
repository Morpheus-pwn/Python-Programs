# Finding the mode of list of numbers(A number that appears most often is the mode.)

numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
numbers.sort()

count = 1
mode = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i-1]:
        count += 1
    else:
        if count > 1:
            mode = numbers[i-1]
        count = 1

print("The mode of the list is:", mode)