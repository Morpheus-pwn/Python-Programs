number = input("Enter a number: ")
sum = 0

for digit in number:
    sum += int(digit)

print("The sum of the digits is:", sum)