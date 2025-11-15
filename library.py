
# Name : Rohit
# Roll number : 2501060098
# Course : Python
# Project : Mini Project Library Inventory and Borrowing System
# Session : 2025-26

library = {}
issued_books = {}

def add_book():
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    copies = int(input("Enter Number of Copies: "))

    library[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }
    print(f"Book '{title}' added successfully!\n")

def view_books():
    print("Library Books")
    print("ID      Title                 Author              Copies")
    print("-" * 55)

    for bid, info in library.items():
        print(f"{bid:<7} {info['title']:<20} {info['author']:<18} {info['copies']:<5}")
    print()

def search_by_id(book_id):
    return library.get(book_id)

def search_by_title(keyword):
    keyword = keyword.lower()
    for bid, info in library.items():
        if keyword in info["title"].lower():
            return bid, info
    return None

def search_book():
    print("Search Book")
    print("1. Search by Book ID")
    print("2. Search by Title")

    choice = input("Enter choice: ")

    if choice == "1":
        srch_id = input("Enter Book ID: ")
        result = search_by_id(srch_id)
        if result:
            print("Book Found:", result)
        else:
            print("Book Not Found")

    elif choice == "2":
        title_part = input("Enter part of title: ")
        result = search_by_title(title_part)
        if result:
            print("Book Found -> ID:", result[0], "Details:", result[1])
        else:
            print("Book Not Found")

def borrow_book():
    print("Borrow Book")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    if book_id not in library:
        print("Book does not exist.")
        return

    if library[book_id]["copies"] > 0:
        library[book_id]["copies"] -= 1
        issued_books[student] = book_id
        print(f"{student} borrowed '{library[book_id]['title']}' successfully.")
    else:
        print("No copies available.")

def return_book():
    print("Return Book")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    if student in issued_books and issued_books[student] == book_id:
        library[book_id]["copies"] += 1
        del issued_books[student]
        print("Book returned successfully.")
    else:
        print("Invalid return details.")

    borrowed_list = [f"{stu} -> {bk}" for stu, bk in issued_books.items()]
    print("Current Borrowed List:", borrowed_list)

def main_menu():
    while True:
        print("===== LIBRARY INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you for using Library Manager!")
            break
        else:
            print("Invalid choice. Try again.")

def load_sample_books():
    samples = {
        "BK01": {"title": "Learn Python", "author": "Guido", "copies": 5},
        "BK02": {"title": "Algorithms Unlocked", "author": "Cormen", "copies": 4},
        "BK03": {"title": "ML Crash Course", "author": "Andrew Ng", "copies": 3},
        "BK04": {"title": "AI Overview", "author": "Stuart Russell", "copies": 2},
        "BK05": {"title": "Deep Learning Insights", "author": "Ian Goodfellow", "copies": 7},
    }
    return samples

if __name__ == "__main__":
    print("Launching Library Application...\n")
    library.update(load_sample_books())
    main_menu()
