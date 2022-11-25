def oddNumbers():
    myList = list(range(1,100))
    return myList[0:100:2]


oddNumbers()


OddNumbersList = oddNumbers()

# OddNumbersList.remove(1)
# OddNumbersList.append(2) 
# OddNumbersList.sort()


# you can use the attribute 'insert' to add a value at a specific position in a list

OddNumbersList.insert(1, 2)

print(OddNumbersList)

# Using while with .pop function

while len(OddNumbersList): # this gets you True as long as the length of that list does not have 0 value [False].
    print(OddNumbersList.pop())

# the above while loop clears all the values inside of that list and gets you an empty list.
print(OddNumbersList)