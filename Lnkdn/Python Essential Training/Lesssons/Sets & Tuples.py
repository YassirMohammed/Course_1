# Sets are either defined using curly brackets or the word set()

mySet1 = {1, 2, 3, "Y" } # values inside can be int or str

print(mySet1)

# casting 
mySet2 = set([1, 2, 3, 5, "S"]) #gets you a set out of a list
mySet3 = set((1, 2, 3, '4')) # gets you a set out of tuple
print(mySet2)
print(mySet3)

# Sets prints you only unique values with repetition.
# So if we have a list of repeated values inside, we can convert it to a set and to back to a list.

myList = [1, 2, 2, 4, 4, 2, 3, 'Y', 'S', 'Y']

# to assign a value in a specific index, do the following:

myList[1] = 'A' # replaces the current value stored in that index with the new assigned one.
print(myList)
mySet = set(myList)

#then you can cast it back to a list;
myNewList = list(mySet)
print(myNewList)


# add elements to a set is permissible, unlike indexing and getting a specific value by referring to its index

mySet.add('R')

print(mySet)

# adding function is not the same as append function which is applied to lists not sets.

# membership operator is applicable to both sets and lists.

print('Y' in mySet) # returns True.

# to remove an element, use 'discard' function

mySet.discard(1)
print(mySet)


# to empty a set, use the following while loop

while len(mySet):
    print(mySet.pop())


# again, this while loop says as long as these is at least one item in that set, just pop one item,
# and so on until it's emptied.


print(mySet)

mySet.discard('Y') # it does not return an error, although the set is empty and does not contain that element
print(mySet)

# Tuple does not suppport element assignment, however, it just support getting that value stored in that index


myTuple = (1, 2, 3)

print(myTuple[1]) # 2


def returnsTuple():
    return 1, 2, 3
    
returnsTuple()
print(type(returnsTuple)) # function, not tuple. [don't know why]

myTuple1 = 1, 2, 3
myTuple2 = (1, 2, 3)

print(type(myTuple1)) # this is actually tuple.
print(type(myTuple2)) # the same


# New term 'Unpacking Values'

# back to the above function

a, b, c = returnsTuple()
print(a)
print(b)
print(c)


