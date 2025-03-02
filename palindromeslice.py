string = input("Enter a string: ")
reversed_string = string[::-1]

if string == reversed_string:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
