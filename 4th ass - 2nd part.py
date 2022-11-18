# Inputs
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

# first and second numbers should be integers
if not first_number.isdigit() and not second_number.isdigit():
    input("Invalid Entry, click Enter to exit")
    exit()

first_num = int(first_number)
second_num = int(second_number)

# operations:

list_of_characters = ["1|+", "2|-", "3|*", "4|/" , "5|^", "6|%"]
for item in list_of_characters:
    print(item)

#getting operation from user
operation_input = input("Choose the suitable character for the operation intended or its corresponding number: ")

#getting results
if operation_input == "1" or operation_input == "+":
    sum_result = first_num + second_num
    print(sum_result)
    sm = input("Would you like to get the integer of the result?(Y or N) ")
    if sm == "Y":
        print(int(sum_result))
elif operation_input == "2" or operation_input == "-":
    sub_result = first_num - second_number
    print(sub_result)
    sb = input("Would you like to get the integer of the result?(Y or N) ")
    if sb == "Y":
        print(int(sub_result))
elif operation_input == "3" or operation_input == "*":
    mult_result = first_num * second_num
    print(mult_result)
    ml = input("Would you like to get the integer of the result?(Y or N) ")
    if ml == "Y":
        print(int(mult_result))
elif operation_input == "4" or operation_input == "/":
    if second_num != 0:
        div_result = first_num / second_num
        print(div_result)
        di = input("Would you like to get the integer of the result?(Y or N) ")
        if di == "Y":
            print(int(div_result))
    elif second_num == 0:
        input("Second number cannot be zero, click Enter to exit")
        exit()
elif operation_input == "5" or operation_input == "^":
    exp_result = first_num ** second_num
    print(exp_result)
    ex = input("Would you like to get the integer of the result?(Y or N) ")
    if ex == "Y":
        print(int(exp_result))
elif operation_input == "6" or operation_input == "%":
    rem_result = first_num % second_num
    print(rem_result)
    re = input("Would you like to get the integer of the result?(Y or N) ")
    if re == "Y":
        print(int(rem_result))   


