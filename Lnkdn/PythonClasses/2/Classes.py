class Purchases:

    
    def add_entry(self, a):
        if a == 'paid':
            self.purchases_list.append([a])
            return self.purchases_list
        
        else:
            self.debt_list.append([a])
            return self.debt_list

    
