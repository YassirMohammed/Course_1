class Client:
    def __init__(self, fullName, age, idNo, phoneNumber):
        self.fullName = fullName
        self.age = age
        self.idNo = idNo
        self.phoneNumber = phoneNumber

    
class Librarian:
    def __init__(self, fullName, age, idNo, employmentType):
        self.fullName = fullName
        self.age = age
        self.idNo = idNo
        self.employmentType = employmentType


class Book:
    def __init__(self, id, title, description, author, status):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.status = status


