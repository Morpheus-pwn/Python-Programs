# Remove duplicate elements from a list.

list = input("Enter a list of elements separated by spaces: ").split()
unique_list = []

for element in list:
    if element not in unique_list:
        unique_list.append(element)

print("List with duplicates removed:", unique_list)
