from collections import defaultdict

# Dictionaries and their properties

dictionaryOfPhones = {
'Samsung': 'A10',
'IPhone': 'I14',
'Xiaomi': 'Note8',
}


# To find a value, you can name the key that it's contained inside

print(dictionaryOfPhones['Samsung'])

# To add a value and a new key

dictionaryOfPhones['Motorolla'] = 'M1'
print(dictionaryOfPhones)

# To replace a value to an existed key

dictionaryOfPhones['Samsung'] = 'S21'
print(dictionaryOfPhones)

# To print only keys or values

print(dictionaryOfPhones.keys())

print(dictionaryOfPhones.values())


# To convert keys or values to a list
# VERY Important!!!
# Casting

listOfKeys = list(dictionaryOfPhones.keys())
listOfValues = list(dictionaryOfPhones.values())

print(listOfKeys)
print(listOfValues)

# If we tried to access a key that's not there, we'll eventually get an error.

# To overcome such an issue, just use the 'get' function

print(dictionaryOfPhones.get('Alienware', 'Not there')) # if you delete 'Not there' it'll get you None 'bool'

print(dictionaryOfPhones) # returns the original dictionary

# the 'get' function uses keys to return their values

print(dictionaryOfPhones.get('Samsung')) # gets you the value of the key 'Samsung'.

# length of a dictionary

print(len(dictionaryOfPhones)) # 4 keys

# You can have a dicitonary of lists instead of string of values.


newDictionaryOfPhones = {
'Samsung': ['A10', 'S21'],
'IPhone': ['I14'],
'Xiaomi': ['Note8', 'Realme', 'Redmi9'],
}


# To add a value to a dicitionary, use 'append' function 
# [VERY IMPORTANT] You must have a list of values inside of the dictionary in order to use the 'append' function

newDictionaryOfPhones['Samsung'].append('A6')

print(newDictionaryOfPhones)

# You can also add a key and a list of values using the assigning way

newDictionaryOfPhones['Motorolla'] = ['M1']

print(newDictionaryOfPhones)


# You can also remove a value by popping its key

newDictionaryOfPhones.pop('Samsung')
print('Removing a key', newDictionaryOfPhones)


# To add a key you're not sure exists, do the following:

if 'Sony' not in newDictionaryOfPhones:
    newDictionaryOfPhones['Sony'] = []

newDictionaryOfPhones['Sony'] = ['SonyErricson']

print(newDictionaryOfPhones)


# the Default dictionary
# you need to import that default dict using 'from collections import defaultdics'

# to create a dictionary using defaultdict, do the following;

fruitsDict = defaultdict(list)

fruitsDict['a'].append('apple')
fruitsDict['b'].append('banana')
fruitsDict['w'].append('watermelon')
print(fruitsDict)


# if you looked up any letter as a key for a dictionary, it'll return empty value and won't return an error.


