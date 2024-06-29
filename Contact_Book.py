class Contact:
    def __init__(self, store_name, phone, email, address):
        self.store_name = store_name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        store_name = input("Enter store name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(store_name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact '{store_name}' has been added successfully!")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.store_name} - {contact.phone}")

    def find_contact(self):
        query = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if query.lower() in contact.store_name.lower() or query in contact.phone]
        if found_contacts:
            for contact in found_contacts:
                print(f"\nStore Name: {contact.store_name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}\n")
        else:
            print("No matching contacts found.")

    def modify_contact(self):
        store_name = input("Enter the store name to update: ")
        for contact in self.contacts:
            if contact.store_name.lower() == store_name.lower():
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print(f"Contact '{store_name}' has been updated successfully.")
                return
        print(f"No contact found with the store name '{store_name}'.")

    def remove_contact(self):
        store_name = input("Enter the store name to delete: ")
        for contact in self.contacts:
            if contact.store_name.lower() == store_name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{store_name}' has been deleted.")
                return
        print(f"No contact found with the store name '{store_name}'.")

def menu():
    book = ContactBook()
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        option = input("Select an option: ")

        if option == '1':
            book.add_contact()
        elif option == '2':
            book.display_contacts()
        elif option == '3':
            book.find_contact()
        elif option == '4':
            book.modify_contact()
        elif option == '5':
            book.remove_contact()
        elif option == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
