from book import Book

class FictionBook(Book):
    def __init__(self, title, author, isbn, genre, category):
        super().__init__(title, author, isbn, genre)
        self.__category = category

    def get_category(self):
        return self.__category

    def __str__(self):
        return f"Fiction - Title: {self.get_title()}, Author: {self.get_author()}, ISBN: {self.get_isbn()}, Category: {self.__category}"