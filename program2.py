# Write a program to remove characters at odd index positions from a string.
def remove(string):
  new_string = ""
  for i in range(len(string)):
    if i % 2 == 0:
      new_string += string[i]
  return new_string

string = input("enter a string: ")
result = remove(string)
print(result)
