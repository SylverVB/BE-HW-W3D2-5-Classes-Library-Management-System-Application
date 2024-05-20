class User:
    def __init__(self, name, library_id):
        self.name = name
        self.__library_id = library_id
        self.borrowed_books = [] # stores book objects - instances of the book class

    def get_library_id(self):
        return self.__library_id

    def show_user_info(self):
        # Displaying user's borrowed books:
        if self.borrowed_books:
            print(f"\nBooks borrowed by {self.name.title()} (Library ID: {self.__library_id}):\n")
            for book in self.borrowed_books:
                print(f"'{book.get_title()}' by {book.get_author()}, ISBN: {book.get_isbn()}")
        else:
            print(f"\n{self.name.title()} (Library ID: {self.__library_id}) has no borrowed books.")