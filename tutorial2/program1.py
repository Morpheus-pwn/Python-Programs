# Write a program to remove all vowel characters from a string.
def remove_vowels(string):
  vowels = "aeiouAEIOU"
  new_string = ""
  for char in string:
    if char not in vowels:
      new_string += char
  return new_string

string = input("Please enter a string: ")
result = remove_vowels(string)
print(result)
