from author import Author
from genre import Genre

class Book:
    def __init__(self, title, author, isbn, genre):
        self.__title = title
        self.__author = author # Author object
        self.__isbn = isbn
        self.__genre = genre # Genre object
        self.__is_available = True
        # Ensure that the author parameter is an instance of the Author class
        if isinstance(author, Author):
            author.add_author_book(self)  # Automatically adds this book to the author's list of books
        else:
            raise ValueError("Author must be an instance of the Author class")
        if not isinstance(genre, Genre):
            raise ValueError("Genre must be an instance of the Genre class")
        
    # Getters and Setters for the above attributes
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_genre(self):
        return self.__genre
    
    def is_available(self):
        return self.__is_available

    def set_is_available(self, availability):
        self.__is_available = availability

    def borrow_book(self):
        if self.is_available(): # Calling the getter to check if self.__is_available is True
            self.set_is_available(False) # calling the setter to change availability to False because the book has been checked out
            return True
        return False
    
    def return_book(self):
        self.set_is_available(True) # self.__is_available = True