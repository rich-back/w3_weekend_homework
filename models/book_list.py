from models.book import *

book1 = Book("Who Moved My Cheese?", "Dr Spencer Johnson", "Self-help")
book2 = Book("The Silmarillion", "J. R. R. Tolkien", "Fantasy Fiction")
book3 = Book("Daft Wee Stories", "Limmy", "Humour")

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def remove_book(book_title):
    book_to_remove = None
    for book in books:
        if book.title == book_title:
            book_to_remove = book
            break

    books.remove(book_to_remove)