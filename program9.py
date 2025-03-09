# Write a Program to reverse the first and second half of a string separately.
string = input("enter a string: ")
first_half = string[:len(string)//2]
second_half = string[len(string)//2:]
reversed_first_half = first_half[::-1]
reversed_second_half = second_half[::-1]
reversed_string = reversed_first_half + reversed_second_half
print(reversed_string)