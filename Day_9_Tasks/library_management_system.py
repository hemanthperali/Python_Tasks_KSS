'''A library stores information about books and digital books. Create a base class Book
with a constructor to initialize book details. Create a derived class EBook that adds file
size information'''

class Book:
    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price

    def display(self):
        print("Book Name:",self.name)
        print("Author:",self.author)
        print("Price:",self.price)

class EBook(Book):
    def __init__(self, file_size):
        self.file_size = file_size
    def display(self):
      print("File_size:",self.file_size)

b = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
b1 = EBook("2MB")
b.display()
b1.display()
        