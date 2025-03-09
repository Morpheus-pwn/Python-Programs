lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

sum_of_odds = 0

for i in range(lower_limit, upper_limit + 1):
    if i % 2 != 0:
        sum_of_odds += i

print("The sum of odd numbers between", lower_limit, "and", upper_limit, "is:", sum_of_odds)
