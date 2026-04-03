# 2. Create a Book class.
# A Book has
#  title
#  author
#  page count

# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.
# Instantiate an instance of the class. You may pass any initial values of your choosing.

class Book:
    # Constructor
    def __init__(self, title, author, page_count):

        self.title = title
        self.author = author
        self.page_count = page_count

    # Getters
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_page_count(self):
        return self.page_count
    
    # Setters
    def set_title(self, new_title):
        self.title = new_title
    def set_author(self, new_author):
        self.author = new_author
    def set_page_count(self, new_page_count):
        self.page_count = new_page_count
    
book1 = Book('How to hack', 'John Doe', 999)

print(book1.get_title())
print(book1.get_author())
print(book1.get_page_count())

print(f'Title: {book1.get_title()}')
print(f'Author: {book1.get_author()}')
print(f'Page count: {book1.get_page_count()}')

print()

book1.set_title('How to hack II')
print(f'New book title: {book1.get_title()}')
