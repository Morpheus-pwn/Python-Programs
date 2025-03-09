# Write a Python program to read list of positive integers and separate the prime and composite numbers.

numbers = input("Enter a list of positive integers separated by spaces: ").split()
prime_numbers = []
composite_numbers = []

for num in numbers:
    num = int(num)
    if num <= 1:
        composite_numbers.append(num)
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
        else:
            composite_numbers.append(num)

print("Prime numbers:", prime_numbers)
print("Composite numbers:", composite_numbers)