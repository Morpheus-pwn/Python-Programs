# Write a Python program to read a list of numbers and sort the list in a nondecreasing
# order without using any built in functions. Separate function should
# be written to sort the list wherein the name of the list is passed as the parameter.

numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
numbers.sort()

print("Sorted list:", numbers)

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers

print("Sorted list using bubble sort:", bubble_sort(numbers))

def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers

print("Sorted list using selection sort:", selection_sort(numbers))

def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i-1
        while j >= 0 and numbers[j] > key:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = key

    return numbers

print("Sorted list using insertion sort:", insertion_sort(numbers))

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("Sorted list using merge sort:", merge_sort(numbers))

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [x for x in numbers[1:] if x < pivot]
    right = [x for x in numbers[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print("Sorted list using quick sort:", quick_sort(numbers))

def heapify(numbers, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and numbers[left] > numbers[largest]:
        largest = left
    if right < n and numbers[right] > numbers[largest]:
        largest = right
    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        heapify(numbers, n, largest)

def heap_sort(numbers):
    n = len(numbers)
    for i in range(n//2 - 1, -1, -1):
        heapify(numbers, n, i)
    for i in range(n-1, 0, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        heapify(numbers, i, 0)
    return numbers

print("Sorted list using heap sort:", heap_sort(numbers))


