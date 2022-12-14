class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def getPrice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price


    def getTitle(self):
        return self.title


    def setDiscount(self, amount):
        self._discount = amount # the attr discount is an internal attr and should not be accessed from outside the class

