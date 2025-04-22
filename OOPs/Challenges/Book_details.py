class Book:
    def __init__(self, title,  author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        return self.title + '\n' + self.author + '\n' + self.price


b1 = Book("The ages of Empire", "Anokond James", '29 $')
print(b1.display())
print(" ")
b2 = Book("The Empire dynasti", "james mark", '$34')
print(b2.display())
