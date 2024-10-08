
# The third exercise of the Django course
# Zahra Abbakhsh

# Definition of Book class
class Book:
    __title: str = None
    __author: str = None
    __isbn: str = None
    __available: bool = True

    def __init__(self, title, author, isbn):
        try:
            self.__title = title
            self.__author = author
            self.__isbn = isbn
        except ValueError | TypeError:
            print('ERROR: Initialization Failed')

    # Define getter function for attributes
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def available(self):
        return self.__available

    # Text display function
    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, ' \
               f'Isbn: {self.isbn}'

    def borrow(self):
        self.__available = False

    def return_book(self):
        self.__available = True


# Definition of Member class
class Member:
    __name: str = None
    __member_id: str = None
    __borrowed_books: [Book] = []

    def __init__(self, name, member_id):
        try:
            self.__name = name
            self.__member_id = member_id
        except ValueError | TypeError:
            print('ERROR: Initialization Failed')

    # Define getter function for attributes
    @property
    def name(self):
        return self.__name

    @property
    def member_id(self):
        return self.__member_id

    @property
    def borrower_books(self):
        return self.__borrowed_books

    # Text display function
    def __str__(self):
        return f'Name: {self.name}, Member ID: {self.member_id}'

    def borrow_book(self, book: Book):
        self.__borrowed_books.append(book)
        book.borrow()

    def return_book(self, book: Book):
        self.__borrowed_books.remove(book)
        book.return_book()


# Definition of Library class
class Library:
    __books: [Book] = None
    __members: [Member] = None

    def __init__(self):
        try:
            self.__books = []
            self.__members = []
        except ValueError | TypeError:
            print('ERROR: Initialization Failed')

    # Define getter function for attributes
    @property
    def books(self):
        return self.__books

    @property
    def members(self):
        return self.__members

    def add_book(self, book: Book):
        self.__books.append(book)

    def register_member(self, member: Member):
        self.__members.append(member)

    def issue_book(self, member_id, isbn):
        this_member: Member = self.find_member(member_id)
        this_book: Book = self.find_book(isbn)

        if this_book.available is True:
            this_member.borrow_book(this_book)
        else:
            print('This Book has borrowed')

    def return_book(self, member_id, isbn):
        this_member: Member = self.find_member(member_id)
        this_book: Book = self.find_book(isbn)

        if this_book.available is False:
            this_member.return_book(this_book)
        else:
            print('This book is not on loan')

    def find_member(self, member_id):
        try:
            for member in self.__members:
                if member.member_id == member_id:
                    return member
            raise FileNotFoundError
        except FileNotFoundError:
            print('No such Member was found...')

    def find_book(self, isbn):
        try:
            for book in self.__books:
                if book.isbn == isbn:
                    return book
            raise FileNotFoundError
        except FileNotFoundError:
            print('No such Book was found')


# The list display function
def print_list(list):
    i = 1
    for item in list:
        print(f'item{i}: {item.__str__()}')
        i += 1


# Create an object from the Book
book1 = Book('1984', 'George Orwell', '1234567890')
print(f'Define a book with these info: {book1.__str__()}')
print('---------------------------------------------------')

# Create an object from the Book
book2 = Book('To Kill a Mockingbird', 'Harper Lee', '0987654321')
print(f'Define a book with these info: {book2.__str__()}')
print('---------------------------------------------------')

# Create an object from the Library
library = Library()
print(f'Define a library with {library.books} book and {library.members}member ')
print('---------------------------------------------------')

# Add a book to the Library Books
library.add_book(book1)
print(f'Add this book: {book1.__str__()} to the library')
print(f'Library Books: ')
print_list(library.books)
print('---------------------------------------------------')

# Add a book to the Library Books
library.add_book(book2)
print(f'Add this book: {book2.__str__()} to the library')
print(f'Library Books: ')
print_list(library.books)
print('---------------------------------------------------')

# Create an object from the Member class
member = Member('Alis', 'M001')
print(f'Define a member with these info: {member.__str__()}')
print('---------------------------------------------------')

# Registering a member and adding him/her to the Library Members
library.register_member(member)
print(f'Register this member: {member.__str__()} to the library')
print(f'Library Members: ')
print_list(library.members)
print('---------------------------------------------------')

# Borrowing books by member
library.issue_book('M001', '1234567890')
print('Borrowing a book with Isbn: 1234567890 by member with ID: M001')
print('---------------------------------------------------')

# Returning the book by the member
library.return_book('M001', '1234567890')
print('Returning a book with Isbn: 1234567890 by member with ID: M001')
print('---------------------------------------------------')
