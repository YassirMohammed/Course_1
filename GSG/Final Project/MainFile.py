from Classes import Client
from Classes import Librarian
fullName = input('What is your full name? ')
age = input('What is your age? ')
idNo = input('What is your ID number? ')
phoneNumber = input('What is your phone number? ')
clientsList = Client(fullName, age, idNo, phoneNumber)

listOfInfo = {'Client Info': [fullName, age, idNo, phoneNumber]}

print(f'Your name is {clientsList.fullName} and your age is {clientsList.age}. Your ID is {clientsList.idNo} and your phone number is {clientsList.phoneNumber}')

print(listOfInfo)