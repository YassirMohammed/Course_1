# Casting
    # convert int to bool
print(bool(0)) # False
print(bool(1)) # True

# Note: anything other than zero to Python will be considered True when casting an int to bool.
print(bool(9)) #True
print(bool(-19)) # True

# Tricky: any value that's considered an int would give you true when converting to bool;
# except when you have 0 in that value or at least part of it. Gives you False.

    # convert str to bool

# anything other than an empty entry will give you True.
# a space is considered a text in this context.
print(bool("")) #False
print(bool("Y")) #any text gives you True

# Every data structures such as; list, dictionary, set, etc, are considered False when converted to bool
# if they were empty. Same as class str.

print(bool(None)) #false! Surprise! ## Exception

# Similar code writing:
# No.1
my_list = [1, 2, 3]
if my_list:
    print("My list has some value in it.")

# No.2
if bool(my_list):
    print("My list has some value in it.")

# No.3
if bool(my_list) == True:
    print("My list has some value in it.")

# The if statement takes the condition as True without notifying.



# Another example:

a = 3
b = 4

if a - b: # this means if the bool value of a - b is true; that is; int not zero
    print("values of a and b are not the same!")

# the only int value that gives False is number 0. 

c = 5
d = 5
if bool(c - d) == False:
    print("a and b have the same values.")

# Ex:
haveUmbrella = True
weatherNice = False

if not haveUmbrella and weatherNice: # not used to negate only the bool next.
    print("Stay Home")
else:
    print('Go out!')