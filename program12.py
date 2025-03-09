# Write Python script for converting Binary number into decimal number.

binary = input("Enter a binary number: ")
decimal = 0
for i in range(len(binary) - 1, -1, -1):
    if binary[i] == '1':
        decimal += 2 ** (len(binary) - 1 - i)

print("Decimal representation:", decimal)