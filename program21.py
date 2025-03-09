# Program to read a string and remove the given words from the string.

string = input("enter a string: ")
words_to_remove = input("enter words to remove (comma-separated): ").split(",")

for word in words_to_remove:
    string = string.replace(word, "")

print("Modified string:", string)
