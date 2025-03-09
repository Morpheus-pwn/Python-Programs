# Write a Program to replace all occurrence of a substring with a new substring.
def replace_substring(string, substring, new_substring):
    return string.replace(substring, new_substring) 

string = input("enter a string: ")
substring = input("enter old substring: ")
new_substring = input("enter new substring: ")
result = replace_substring(string, substring, new_substring)
print(f"String after replacing '{substring}' with '{new_substring}': {result}")