# Program to read list of names and sort the list in alphabetical order.

def sort_names():
  names = []
  while True:
    name = input("Enter a name (or type 'done' to finish): ")
    if name.lower() == 'done':
      break
    names.append(name)

  names.sort()
  return names

sorted_names = sort_names()
print("Sorted names:")
for name in sorted_names:
  print(name)

