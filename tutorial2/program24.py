# Program to remove all duplicate elements from a list

def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
unique_numbers = remove_duplicates(numbers)

print("List with duplicates removed:", unique_numbers)