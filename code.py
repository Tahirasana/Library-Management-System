books = []
status = []
borrower = []

def add_book():
    name = input("Enter book name: ")
    books.append(name)
    status.append("Available")
    borrower.append("---")
    print(f"Book '{name}' added successfully!")

def show_all_books():
    if len(books) == 0:
        print("No books in library!")
        return
    print("\n------- ALL BOOKS -------")
    print(f"{'ID':<5} {'Book Name':<20} {'Status':<12} {'Borrower'}")
    print("-" * 50)
    for i in range(len(books)):
        print(f"{i+1:<5} {books[i]:<20} {status[i]:<12} {borrower[i]}")

def search_book():
    search = input("Enter book name to search: ")
    found = False
    for i in range(len(books)):
        if books[i].lower() == search.lower():
            print("\nBook Found!")
            print(f"   Book Name : {books[i]}")
            print(f"   Status    : {status[i]}")
            print(f"   Borrower  : {borrower[i]}")
            found = True
            break
    if found == False:
        print("Book not found in library!")

def issue_book():
    name = input("Enter book name to issue: ")
    for i in range(len(books)):
        if books[i].lower() == name.lower():
            if status[i] == "Available":
                borrower_name = input("Enter borrower name: ")
                status[i] = "Issued"
                borrower[i] = borrower_name
                print(f"Book '{books[i]}' issued to {borrower_name}!")
            else:
                print(f"Sorry! Book already issued to {borrower[i]}")
            return
    print("Book not found in library!")

def return_book():
    name = input("Enter book name to return: ")
    for i in range(len(books)):
        if books[i].lower() == name.lower():
            if status[i] == "Issued":
                print(f"Book '{books[i]}' returned from {borrower[i]}!")
                status[i] = "Available"
                borrower[i] = "---"
            else:
                print("This book was not issued to anyone!")
            return
    print("Book not found in library!")

def main_menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thankyou! Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-6")

main_menu()