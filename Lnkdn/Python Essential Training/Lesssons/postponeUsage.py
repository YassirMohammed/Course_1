from datetime import datetime


firstNameTime = datetime.now().second + 1
secondNameTime = datetime.now().second + 3


while datetime.now().second != firstNameTime:
    pass
print('My name is: ')

while datetime.now().second != secondNameTime:
    pass
print('Yassir Muhammad')
