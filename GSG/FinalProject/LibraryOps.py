from ClientsClass import Clients
from LibrarianClass import Librarian

class ClientOps:
    clients_list:list[Clients] = []

    id_counter = 0

    def add_client(self, full_name:str, age:int, id_no, phone_number):


        if full_name.isspace() or full_name == None:
            print('Invalid input')

        else:
            client_name = Clients(full_name=full_name, age=age, id_no=id_no, phone_number=phone_number,identifier=self.id_counter)
            self.id_counter = self.id_counter + 1
            self.clients_list.append(client_name)

class LibrarianOps():
    librarians_list:list[Librarian] = []


    def add_librarian(self, full_name:str, age:int, id_no, employment_type):


        if full_name.isspace() or full_name == None:
            print('Invalid input')

        else:
            librarian_name = Librarian(full_name=full_name, age=age, id_no=id_no, employment_type=employment_type,identifier=self.id_counter)
            self.id_counter = self.id_counter + 1
            self.librarians_list.append(librarian_name)
