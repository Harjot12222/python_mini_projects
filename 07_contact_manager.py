contacts = {}

def add_contact():
    name = input("Enter the contact name: ").strip()
    number = input("Enter the phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name.lower()] = {"name": name, "number": number, "email": email}
    print(f"✅ Contact '{name}' added.")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
        return
    for i, contact in enumerate(contacts.values(), start=1):
        print(f"{i}. Name: {contact['name']}, Number: {contact['number']}, Email: {contact['email']}")

def search_contact():
    search = input("Enter the contact name to search: ").strip().lower()
    contact = contacts.get(search)
    if contact:
        print(f"Found: Name: {contact['name']}, Number: {contact['number']}, Email: {contact['email']}")
    else:
        print("❌ No such contact found.")

def update_contact():
    search = input("Enter the contact name to update: ").strip().lower()
    if search not in contacts:
        print("❌ No such contact found.")
        return
    contact = contacts[search]
    print("Leave a field empty to keep it unchanged.")
    new_name = input(f"New name [{contact['name']}]: ").strip()
    new_number = input(f"New number [{contact['number']}]: ").strip()
    new_email = input(f"New email [{contact['email']}]: ").strip()
    
    if new_name:
        contacts[new_name.lower()] = contacts.pop(search)
        contact = contacts[new_name.lower()]
        contact["name"] = new_name
    if new_number:
        contact["number"] = new_number
    if new_email:
        contact["email"] = new_email
    print(f"✅ Contact updated: {contact}")

def delete_contact():
    search = input("Enter the contact name to delete: ").strip().lower()
    if search in contacts:
        deleted = contacts.pop(search)
        print(f"✅ Contact '{deleted['name']}' deleted.")
    else:
        print("❌ Contact not found.")

# Main loop
while True:
    print("\n__Contacts__")
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update existing contact")
    print("5. Delete contact by name")
    print("6. Quit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thanks, have a great day ❤️")
        break
    else:
        print("Invalid choice T_T")
