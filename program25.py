# Consider a list consisting of integers, floating point numbers and strings.
# Separate them into different lists depending on the data.

list = input("Enter a list of elements separated by spaces: ").split()
int_list = []
float_list = []
string_list = []

for element in list:
    try:
        int_list.append(int(element))
    except ValueError:
        try:
            float_list.append(float(element))
        except ValueError:
            string_list.append(element)

print("Integer list:", int_list)
print("Float list:", float_list)
print("String list:", string_list)
