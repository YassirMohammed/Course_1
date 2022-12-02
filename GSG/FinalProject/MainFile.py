from ClientsClass import Clients

class LibraryOperations:
    clients_list:list[Clients] = []


    def add_client(self, full_name, age, id_no, phone_number):
        client_name = Clients(full_name=full_name, age=age, id_no=id_no, phone_number=phone_number,identifier=len(self.clients_list))
        self.clients_list.append(client_name)
