books = []


def addBook(title,author):
    books.append({"title" : title, "author" : author, "borrow" : False})
    print(f"Book {title} by {author}")



def view_books():
    if not books:
        print("Library is Empty: ")
    else:
        for book in books:
            if not book['borrowed']:
                status = "Available"
            else:
                status = "Borrow"
            print(f"{book['title']} by {book['author']} {status}")



def search_by_title(title):
    found_book = [book for book in books if title.lower() in book['title'].lower()]
    if found_book:
        print("Match Books Found: ")
        for book in found_book:
            print(f"{book['title']} by {book['author']} [{'Available' if not book['borrowed'] else 'Borrowed'}]")
    else:
        print("No Books Found with title: ")


def search_by_author(author):
    found_book = [book for book in books if author.lower() == book['author']]
    if found_book:
        for book in found_book:
            print(f"{book['title']} by {book['author']} [{'Available' if not book['borrowed'] else 'Borrowed'}]")
    else:
        print("Not Found Books: ")


def borrow_book(title):
    for book in books:
        if book['title'].lower() in title.lower():
            book['borrowed'] = True
            print("Successfully Borrowed! ") 
        else:
            print(f"Book {title} is not avaliable: ")
    else:
        print("Book not found in the library: ")
        
def return_book(title):
    for book in books:
        if book['title'].lower() == title.lower():
            book['borrowed'] = False
            print(f"book {title} Successfully return")
        else:
            print(f"Book {title} is already in the library. ")
    else:
        print(f"Book not Found in library: ")
        
def main():
    while True:
        print("\n1. Add Book")
        print("2. View Books")
        print("3. Search by Title")
        print("4. Search by Author")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            addBook(title, author)
        elif choice == '2':
            view_books()
        elif choice == '3':
            title = input("Enter the title to search for: ")
            search_by_title(title)
        elif choice == '4':
            author = input("Enter the author to search for: ")
            search_by_author(author)
        elif choice == '5':
            title = input("Enter the title of the book to borrow: ")
            borrow_book(title)
        elif choice == '6':
            title = input("Enter the title of the book to return: ")
            return_book(title)
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
