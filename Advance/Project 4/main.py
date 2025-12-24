#Contact Book
def add_contact():
def view_contacts():
def search_contact():
def delete_contact():
        
def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_contact(contacts, name, phone, email)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(contacts, name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()