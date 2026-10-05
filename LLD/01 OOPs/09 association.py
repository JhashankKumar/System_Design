"""
Association is a relationship between two classes that allows one class to use the functionality 
of another class. It represents a "has-a" relationship, where one class contains a reference to 
another class. In this example, we have a Library class that has an association with the Book class. 
The Library class can contain multiple Book objects, and each Book object is associated with a 
specific Library.

In this example, we have a `Library` class that has an association with the `Book` class. 
The `Library` class can contain multiple `Book` objects, and each `Book object is associated 
with a specific `Library`. This allows for better organization and management of books within a 
library, as each book can be linked to its corresponding library. The association between the 
two classes is established through the use of references, allowing for easy access and manipulation 
of the related objects.
"""
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            print(f" - {book.title}")


class Book:
    def __init__(self, title, library):
        self.title = title
        self.library = library

    def show_library(self):
        print(f"{self.title} is in {self.library.name}")


if __name__ == "__main__":
    library = Library("City Library")

    book1 = Book("1984", library)
    book2 = Book("Brave New World", library)

    library.add_book(book1)
    library.add_book(book2)

    library.show_books()
    book1.show_library()
    book2.show_library()