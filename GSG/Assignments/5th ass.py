# Solution 1


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]



newDictionary = {keys[0]: values[0], keys[1]: values[1], keys[2]: values[2]}

print(newDictionary)



# Solution 2

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# newDictionary = {}
# for i in keys:
#     newDictionary[i] = []

# newDictionary['Ten'] = values[0]
# newDictionary['Twenty'] = values[1]
# newDictionary['Thirty'] = values[2]

# print(newDictionary)


# NewValues = [int(input("Enter Ten: ")), int(input("Enter Twenty: ")), int(input("Enter Thirty: "))]

# print(NewValues)



######################
# To remove a key from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}


sample_dict.pop('name')
sample_dict.pop('salary')

print(sample_dict)




###########################

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]


for i in sample_list:
    sample_set.add(i)


print(sample_set)


################################

#union and intersection

#Not done yet



##############################


tuple1 = (10, 20, 30, 40, 50)


#get reverse [worked but not reversed back to tuple; returned a set reversed]

listofTuple = list(tuple1)

a = listofTuple.reverse()

print(listofTuple)


####################################

# access value 20 from the next tuple

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))


listInTuple1 = tuple1[1]

print(listInTuple1[1])

###################################


# unpack the tuple

tuple1 = (10, 20, 30, 40)


aTuple = print(tuple1[0])
bTuple = print(tuple1[1])
cTuple = print(tuple1[2])
dTuple = print(tuple1[3])

##################################3


