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
print('Choose one of the following arithmetic operations: ')
list_of_characters = ["1|+", "2|-", "3|*", "4|/" , "5|^", "6|%"]
for item in list_of_characters:
    print(item)
print("")

#getting operation from user
operation_input = input("Choose the suitable character for the operation intended or its corresponding number: ")

#getting results
if operation_input == "1" or operation_input == "+":
    sum_result = first_num + second_num
    print(sum_result)
    sm = input("Would you like to get the integer of the result or the round?(i or r) ")
    if sm == "i":
        print(int(sum_result))
    elif sm == "r":
        print(round(sum_result))
    else:
        input("Click Enter to exit")
        exit() 
elif operation_input == "2" or operation_input == "-":
    sub_result = first_num - second_num
    print(sub_result)
    sb = input("Would you like to get the integer of the result or the round?(i or r) ")
    if sb == "i":
        print(int(sub_result))
    elif sb == "r":
        print(round(sub_result))
    else:
        input("Click Enter to exit")
        exit() 
elif operation_input == "3" or operation_input == "*":
    mult_result = first_num * second_num
    print(mult_result)
    ml = input("Would you like to get the integer of the result or the round?(i or r) ")
    if ml == "i":
        print(int(mult_result))
    elif ml == "r":
        print(round(mult_result))
    else:
        input("Click Enter to exit")
        exit() 
elif operation_input == "4" or operation_input == "/":
    if second_num != 0:
        div_result = first_num / second_num
        print(div_result)
        di = input("Would you like to get the integer of the result or the round?(i or r) ")
        if di == "i":
            print(int(div_result))
        elif di == "r":
            print(round(div_result))
        else:
            input("Click Enter to exit")
            exit() 
    elif second_num == 0:
        input("Second number cannot be zero, click Enter to exit")
        exit()
elif operation_input == "5" or operation_input == "^":
    exp_result = first_num ** second_num
    print(exp_result)
    ex = input("Would you like to get the integer of the result or the round?(i or r) ")
    if ex == "i":
        print(int(exp_result))
    elif ex == "r":
        print(round(exp_result))
    else:
        input("Click Enter to exit")
        exit() 
elif operation_input == "6" or operation_input == "%":
    rem_result = first_num % second_num
    print(rem_result)
    re = input("Would you like to get the integer of the result or the round?(i or r) ")
    if re == "i":
        print(int(rem_result))
    elif re == "r":
        print(round(rem_result))
    else:
        input("Click Enter to exit")
        exit()   


