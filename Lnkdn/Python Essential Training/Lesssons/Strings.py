import math
# Slicing

    # Strings

txt = 'My name is Yassir'

print(txt[11:]) # you can define the start and leave it for python to define the end of the characters.

    #lists

myList = [1, 3, 4, 6]

print(myList[2:]) # only 0, 1, 2, 3 placeholders [You can leave the last undefined or write down a number that's
                    # more than the actual list's length

print(len(txt))
print(len(myList))

# Formatting

print('My number is: ' + str(5)) #this line can be done using the following...

print(f'My number is: {5}')  # you can put your variables inside {curly braces}

#  You can also include expressions inside curly braces.

print(f'My number is: {5} and twice that is {5*2}')

# We can do pi rounded to 2 decimal places with a colon and a .2f [.2f = .3 for some reason]
print(f'Pi is: {math.pi}') # this gets you the 15 decimal places.
print(f'Pi is: {math.pi:.2f}')

# old python syntax for this formatting was...
oldFormatting = 'Pi is: '.format(math.pi) #does not work for me [don't know why]
print(oldFormatting)

# Multi-line Strings
# If you use string between 3 quotes, you can write down line after line by simply hitting Enter.

print('''
    Hi there,

My Name's Yassir Muhammad.
This is my first programming language to learn.

''')
#So flexible!!!