# Write a program to replace all the spaces in the input string with * or if no
# spaces found, put $ at the start and end of the string.
def replace_spaces(string):
  if ' ' in string:
    return string.replace(' ', '*')
  else:
    return '$' + string + '$'

string1 = input("enter a string: ")
string2 = input("enter another string: ") 

print(f"Modified string 1: {replace_spaces(string1)}")
print(f"Modified string 2: {replace_spaces(string2)}")