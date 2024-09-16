
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

    ...


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

    ...


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

    ...
