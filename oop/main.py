from library_system import Book, EBook, PrintBook, Library

def main():
    library = Library()
    
    # Adding different types of books to the library
    library.add_book(EBook("The Digital Fortress", "Dan Brown", 500))
    library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 277))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    
    # Listing all books in the library
    library.list_books()

if __name__ == "__main__":
    main()
