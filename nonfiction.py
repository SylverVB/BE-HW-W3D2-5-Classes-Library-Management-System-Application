from book import Book

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, genre, subject):
        super().__init__(title, author, isbn, genre)
        self.__subject = subject
        # The subject attribute is commonly associated with non-fiction works and represents the specific subject matter of the nonfiction book. 
        # For example, if you have a nonfiction book about history, the subject might be "History". Other examples of subjects might be "Science", "Biography", "Self-Help", "Technology", etc.

    def get_subject(self):
        return self.__subject

    def __str__(self):
        return f"Nonfiction - Title: {self.get_title()}, Author: {self.get_author()}, ISBN: {self.get_isbn()}, Subject: {self.__subject}"