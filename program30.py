# Program to completely remove duplicate elements without keeping any copy.

def remove_duplicates_inplace(input_list):
  seen = set()
  i = 0
  while i < len(input_list):
    if input_list[i] in seen:
      del input_list[i]
    else:
      seen.add(input_list[i])
      i += 1

my_list = input("Enter a list of elements separated by spaces: ").split()
remove_duplicates_inplace(my_list)
print(f"List after removing duplicates: {my_list}") 

