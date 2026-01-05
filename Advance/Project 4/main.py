# Contact Book
import json
import os

DATA_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def search_contact(contacts, name):
    if name in contacts:
        info = contacts[name]
        print(f"Found: Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print(f"Contact {name} not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")
        
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