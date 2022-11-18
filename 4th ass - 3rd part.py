no1 = input("1st Number: ")
no2 = input("2nd Number: ")
no3 = input("3rd Number: ")
no4 = input("4th Number: ")
no5 = input("5th Number: ")

list1 = [no1, no2, no3, no4, no5]

list1.sort()
length_for_last_input = len(list1)

mini = list1[0]
maxi = list1[length_for_last_input-1]

print("Minimum value is:", mini)
print("Maximum value is:", maxi)
