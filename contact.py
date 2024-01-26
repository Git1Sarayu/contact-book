import json

# Function to load contacts from a file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

# Function to save contacts to a file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

# Function to view all contacts
def view_contacts():
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")
        for key, value in contact.items():
            print(f"{key}: {value}")

# Function to search for a contact
def search_contact():
    query = input("Enter the contact's name or phone number to search: ")
    found_contacts = []

    for contact in contacts:
        if query.lower() in contact["Name"].lower() or query in contact["Phone"]:
            found_contacts.append(contact)

    if found_contacts:
        print("\nFound Contacts:")
        for i, found_contact in enumerate(found_contacts, start=1):
            print(f"\nContact {i}:")
            for key, value in found_contact.items():
                print(f"{key}: {value}")
    else:
        print("No matching contacts found.")

# Function to update a contact
def update_contact():
    view_contacts()
    try:
        index = int(input("\nEnter the index of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            for key in contacts[index]:
                contacts[index][key] = input(f"Enter new {key}: ")
            save_contacts(contacts)
            print("Contact updated successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Function to delete a contact
def delete_contact():
    view_contacts()
    try:
        index = int(input("\nEnter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            print(f"Deleted Contact:")
            for key, value in deleted_contact.items():
                print(f"{key}: {value}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Main program
contacts = load_contacts()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
