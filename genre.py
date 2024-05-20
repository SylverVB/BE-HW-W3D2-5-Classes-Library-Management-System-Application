class Genre:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__categories = {}  # Using a dictionary to store categories and their books

    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_categories(self):
        return self.__categories
    
    def add_category(self, category):
        if category not in self.__categories:
            self.__categories[category] = []

    def add_book_to_category(self, category, book): # adding a book to the appropriate category within the genre
        if category in self.__categories:
            self.__categories[category].append(book)
        else:
            self.__categories[category] = [book]

    # Using a string representation method to provide a meaningful and informative representation of genre objects when they are converted to strings:
    def __str__(self):
        return f"Genre: {self.get_name()}, Description: {self.get_description()}, Categories: {', '.join(self.__categories.keys())}"