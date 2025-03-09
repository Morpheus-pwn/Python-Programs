# Write Python script for converting decimal number into Binary number.

decimal = int(input("Enter a decimal number: "))
binary = ""
while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2

print("Binary representation:", binary)