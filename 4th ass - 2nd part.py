# Inputs
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

# first and second numbers should be integers
if not first_number.isdigit() and not second_number.isdigit():
    input("Invalid Entry, click Enter to exit")
    exit()
else:
    first_num = int(first_number)
    second_num = int(second_number)

# operations:
dictionary_of_operations = {1: "+", 2: "-", 3: "*", 4: "/" , 5: "**", 6: "%"}
sum = first_num + second_num
sub = first_num - second_num

