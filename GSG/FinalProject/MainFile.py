from LibraryOps import ClientOps
from LibraryOps import LibrarianOps

client_name = ClientOps()
librarian_name = LibrarianOps()

print('Hello Dear User')

ask_what_to_do = input('Do you want to add client or librarian? "C for Client, L for Librarian"')

if ask_what_to_do == 'C':

    def get_client_info():

        full_name = input('Enter your name: ')
        age = input('Enter your age: ')
        id_no = input('Enter your ID: ')
        phone_number = input('Enter your phone number: ')
        client_name.add_client(full_name=full_name, age=age, id_no=id_no, phone_number=phone_number)



    get_client_info()

elif ask_what_to_do == 'L':
    def get_librarian_info():

        full_name = input('Enter your name: ')
        age = input('Enter your age: ')
        id_no = input('Enter your ID: ')
        employment_type = input('Enter your employment type: ')
        librarian_name = LibrarianOps.add_librarian(full_name=full_name, age=age, id_no=id_no, employment_type=employment_type)



    get_librarian_info()
