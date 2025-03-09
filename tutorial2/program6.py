# Write a program to remove all occurrence of a substring from a string.
def remove_substring(string, substring):

  while substring in string:
    string = string.replace(substring, "")
  return string

string = input("enter a string: ")
substring = input("enter substring: ")
result = remove_substring(string, substring)
print(f"String after removing '{substring}': {result}")
