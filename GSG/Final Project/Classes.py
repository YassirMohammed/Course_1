class Client:
    def __init__(self, id:int, fullName:str, age:int, phone_number:int):
        self.id = id
        self.fullName = fullName
        self.age = age
        self.phone_number = phone_number


    
class Librarian:
    def __init__(self, id, fullName, age, id_no, employment_type:bool):
        self.id = id
        self.fullName = fullName
        self.age = age
        self.id_no = id_no
        self.employment_type = employment_type

    def get_employment_type(self):
        if self.employment_type == True:
            return 'Full'
        else:
            return 'Part'


class Book:
    def __init__(self, id, title, description, author, status):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.status = status

    def get_status(self):
        if self.status == True:
            return 'Available'
        else:
            return 'Not Available'


class Borrowing_Order(Book):
    def __init__(self, id, date, client_id, book_id, status):
        self.id = id
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.status = status


    def create_borrow_order(self):
        self.book_id = Book

    





