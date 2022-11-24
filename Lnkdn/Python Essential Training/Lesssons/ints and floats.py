#Python always return floats from division because there's a potential to get a non-integer number.
#Any operation containing a float should give you a float even if it's not a division operation.

#To get an integer from an operation containing float, simply include it inside the int() class.
#Ex:
print(3 + 4.2) #gets you a float
print("int class")
print(int(3 + 4.2)) #gets you an integer



#Classes in python include: strings, integers, floats, lists.
#So, when converting from a class to another, you do what programmers call "Casting".
#When casting from a float to an int, python does not take numbers after the point into consideration and just throws that part away
#In other words, integer does not round for you.

#round function does give you the number close to the actual float number. For ex;
print("Round Function")
print(round(14/3)) # int would give you 4 instead.

# You can pass the number of the decimal places you want to round up to.

result1 = round(14/3, 2) # this indicates that the result would get you the number including only the first 2 decimal digits.
print(result1)
#So, again, this operation gets you the division of 14 over 3 having only 2 decimal digits.

#There's an issue Python is not dealing very well with. 
# Ex;
print(1.2 - 1) # the result would be 0.19999 not 0.2 because python gives you a value that's close to the actual one.

#To overcome such an issue, use the round function with the approximation of 2 decimal values as below.

print(round(1.2 - 1, 2))



###########################

# Other types of numbers:
# If you pass a string number to an int class, string will be converted to integer

a = "100"
b = int(a)
print(type(a))
print(type(b))

# Converting to binary or base 16 'thuna'i, sadis 3ashri'

# Since hexadecimal or base 16 is consisted of [0, 1, 2, ..., a, b, .. f], we should take this code as a string
# To convert that string to a number in base 16 or binary systems, use the int() function and add a comma 
# followed by 2 [for binary] and 16 for [hexadecimal]

print(int("1001", 2)) #binary
print(int("1ab", 16)) # base 16


# Decimal Module

# You should keep the next line above your code when dealing with numbers that must be accurate to avoid the weakness in floats.

from decimal import Decimal, getcontext # Decimal is a class, and getcontext is a function that are already there in Python.
# You can refer to the documentation to get more info about this subject.


