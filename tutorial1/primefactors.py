num = int(input("Enter a number: "))

print("Prime factors of", num, "are:")
for i in range(2, int(num**0.5) + 1):
    while num % i == 0:
        print(i)
        num //= i
if num > 1:
    print(num)
