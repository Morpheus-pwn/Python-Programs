# Write a menu driven program to implement the following
# i)check even or odd
# ii)check number is positive negative or zero
# iii) generate factors of a number

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_positive_negative_zero(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def generate_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def main():
    while True:
        print("Menu:")
        print("1. Check even or odd")
        print("2. Check positive, negative or zero")
        print("3. Generate factors")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            num = int(input("Enter a number: "))
            result = check_even_odd(num)
            print(f"{num} is {result}.\n")
        elif choice == 2:
            num = int(input("Enter a number: "))
            result = check_positive_negative_zero(num)
            print(f"{num} is {result}.\n")
        elif choice == 3:
            num = int(input("Enter a number: "))
            factors = generate_factors(num)
            print(f"Factors of {num} are: {factors}\n")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
    print("Exiting the program.\n")
    exit(0)

