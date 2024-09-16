
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