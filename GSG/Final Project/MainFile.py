from Classes import Client
from Classes import Librarian
from Classes import Book

new_client = Client(id=1, fullName='Yassir Muhammad', age=29, phone_number= 592574153)
new_librarian = Librarian(id=1, fullName='Yassir Muhammad', id_no=999, age=29, employment_type = True)

book1 = Book(id=1, title='The Subtle Art', description='Self-Development', author='Person1', status= True)
book2 = Book(id=2, title='Islamic History', description='History', author='Person2', status= True)
book3 = Book(id=3, title='History of Palestine', description='History', author='Person3', status= False)
book4 = Book(id=4, title='Comparative Literature', description='English Language', author='Person4', status= True)



print([book1.title, book2.title, book3.title, book4.title])

print(new_librarian.get_employment_type())