for num in range(100, 1001):
    sum_of_digits = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit
        temp //= 10
    if sum_of_digits % 9 == 0:
        print(num)
