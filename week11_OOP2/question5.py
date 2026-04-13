class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_author(self):
        return self.author
    
    def set_author(self, new_author):
        self.author = new_author
    
    def display_info(self):
        print(f'Title: {self.title}, Author: {self.author}')

    def __str__(self):
        print (f'Book(title={self.title}, author={self.author})')
    
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
            self.books.append(book)
    
    def display_catalog(self):
        for book in self.books:
            book.display_info()

    def __str__(self):
        return f'Libray(library_name = {self.library_name})' 

book_1 = Book('Computer Engr for Nerds', 'KM')
book_2 = Book('Mathematics for Nerds', 'KM')

library_1 = Library('Memorial Hall')

library_1.add_book(book_1)
library_1.add_book(book_2)

library_1.display_catalog()
print(library_1)
