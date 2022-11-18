# Welcome
print('Hi there!, please add the info requested below...')

# inputs
name = input("Enter your name: ")
if name.isspace() or name.isdigit():
    input("Input wrong, click Enter to exit...")
    exit()
age = input("Enter your age: ")
if age.isspace():
    input("Input wrong, click Enter to exit....")
    exit()
if not age.isdigit():
    input("Input wrong, click Enter to exit....")
    exit()
age_number = int(age)

address = input("Enter your address:")

print("Hello Mr.", name)
print('Your age is', age_number, "and your address is: ", address)
