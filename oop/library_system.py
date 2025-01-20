# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize a book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an eBook with title, author, and file size."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the eBook."""
        return f"'{self.title}' by {self.author}, {self.file_size}MB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a print book with title, author, and page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book."""
        return f"'{self.title}' by {self.author}, {self.page_count} pages"


class Library:
    def __init__(self):
        """Initialize the library with an empty book collection."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            print(book)
