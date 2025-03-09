# Write a program to slice the string into two separate strings; one with all the
# characters in the odd indices and one with all characters in even indices.
def split_string_by_index(string):
  even_string = ""
  odd_string = ""
  for i in range(len(string)):
    if i % 2 == 0:
      even_string += string[i]
    else:
      odd_string += string[i]
  return even_string, odd_string

string = input("enter a string: ")
even_chars, odd_chars = split_string_by_index(string)
print(f"Even index characters: {even_chars}")
print(f"Odd index characters: {odd_chars}")