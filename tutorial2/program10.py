# Write a Python program to check the validity of a password given by the user
# The Password should satisfy the following criteria:
# 1. Contains at least one letter between a and z
# 2. Contains at least one number between 0 and 9
# 3. Contains at least one letter between A and Z
# 4. Contains at least one special character from $, #, @
# Minimum length of password: 6 

import re
password = input("Enter a password: ")

if len(password) < 6:
    print("Password must be 6 characters long.")
    exit()

if not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter.")
    exit()

if not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
    exit()

if not re.search("[0-9]", password):
    print("Password must contain at least one number.")
    exit()

if not re.search("[#$@]", password):
    print("Password must contain at least one special character.")
    exit()

print("Password is valid.")
