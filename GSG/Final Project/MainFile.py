from Classes import Client
from Classes import Librarian
from Classes import Book
from Classes import Borrowing_Order


new_client = Client(id=1, fullName='Ahmed', age=29, phone_number= 592574153)
new_librarian = Librarian(id=1, fullName='Yassir Muhammad', id_no=999, age=33, employment_type = False)

book1 = Book(id=1, title='The Subtle Art', description='Self-Development', author='Person1', status= True)
book2 = Book(id=2, title='Islamic History', description='History', author='Person2', status= True)
book3 = Book(id=3, title='History of Palestine', description='History', author='Person3', status= False)
book4 = Book(id=4, title='Comparative Literature', description='English Language', author='Person4', status= True)

list_of_books = [book1.title, book2.title, book3.title, book4.title]
list_of_clients = [new_client]
list_of_librarians = [new_librarian]
list_of_borrowed_orders = []


dictionary_of_books = {
    book1: [book1.id, book1.title, book1.description, book1.author, book1.status],
    book2: [book2.id, book2.title, book2.description, book2.author, book2.status],
    book3: [book3.id, book3.title, book3.description, book3.author, book3.status],
    book4: [book4.id, book4.title, book4.description, book4.author, book4.status]
}


print(list_of_books)

print(f'Type of employment for the librarian is: {new_librarian.get_employment_type()}')

# ask client which book to borrow

ask_client_which_book = input('Which of the above books you want to borrow? ')

# check if book is available for borrowing from the above dictionary.

if dictionary_of_books[book1][1] == ask_client_which_book:
    if (dictionary_of_books[book1][4]) == True:
        ask_for_id_info = input('What is your id? ')
        if int(ask_for_id_info) == new_client.id:
            Borrowing_Order.create_borrow_order(self=1)            

elif dictionary_of_books[book2][1] == ask_client_which_book:
    if (dictionary_of_books[book2][4]) == True:
        ask_for_id_info = input('What is your id? ')
        if int(ask_for_id_info) == new_client.id:
            Borrowing_Order.create_borrow_order(self=1) 


elif dictionary_of_books[book3][1] == ask_client_which_book:
    if (dictionary_of_books[book3][4]) == True:
        ask_for_id_info = input('What is your id? ')
        if int(ask_for_id_info) == new_client.id:
            Borrowing_Order.create_borrow_order(self=1) 

elif dictionary_of_books[book4][1] == ask_client_which_book:
    if (dictionary_of_books[book4][4]) == True:
        ask_for_id_info = input('What is your id? ')
        if int(ask_for_id_info) == new_client.id:
            Borrowing_Order.create_borrow_order(self=1) 

else:
    print('input wrong or book is unavilable. Choose another book and check again')
