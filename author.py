class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
        self.author_books = []  # List to store books written by the author

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def add_author_book(self, book):
        self.author_books.append(book)

    def show_author_info(self):
        print(f"\nAuthor: {self.__name}")
        print(f"Biography: {self.__biography}")
        print("Books:")
        for book in self.author_books:
            print(f" - {book.get_title()}")
        if not self.author_books:
            print(f" - No books added yet!")

    def __str__(self):
        return self.__name