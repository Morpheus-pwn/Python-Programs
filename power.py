def power(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / power(x, -y)
    else:
        result = 1
        for i in range(y):
            result *= x
        return result

x = int(input("Enter the base: "))
y = int(input("Enter the exponent: "))

result = power(x, y)
print(x, "^", y, "=", result)
