numbers = []
for i in range(4):
    number = int(input(f"Enter integer {i+1}: "))
    numbers.append(number)

sum_positive = 0
sum_negative = 0

for number in numbers:
    if number > 0:
        sum_positive += number
    elif number < 0:
        sum_negative += number

average_positive = sum_positive / len([number for number in numbers if number > 0]) if sum_positive else 0
average_negative = sum_negative / len([number for number in numbers if number < 0]) if sum_negative else 0

print(f"Sum of positive numbers: {sum_positive}")
print(f"Sum of negative numbers: {sum_negative}")
print(f"Average of positive numbers: {average_positive}")
print(f"Average of negative numbers: {average_negative}")

