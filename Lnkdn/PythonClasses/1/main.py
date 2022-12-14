from Classes import Book


b1 = Book('Peace and War', 33)

b2 = Book('Palestine and Peace', 35)



print('b2 price', b2.getPrice())

b2.setDiscount(.25)

print('b2 price after the discount', b2.getPrice())


#### the double underscore prevents overwriting the attribute with double underscore.


