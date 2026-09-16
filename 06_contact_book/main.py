# Simple Contact Book
# Student Level Pure Python Project

contacts = []

def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email (optional): ").strip()

    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })
        print("✅ Contact saved!")
    else:
        print("❌ Name and Phone are required.")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
        return

    print("\n----- All Contacts -----")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")

def search_contact():
    keyword = input("Enter name or phone to search: ").strip().lower()
    found = False

    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            print(f"Found → {c['name']} | {c['phone']} | {c['email']}")
            found = True

    if not found:
        print("❌ No contact found.")

def delete_contact():
    view_contacts()
    if not contacts:
        return

    try:
        num = int(input("Enter contact number to delete: "))
        if 1 <= num <= len(contacts):
            removed = contacts.pop(num - 1)
            print(f"🗑️ Deleted: {removed['name']}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose (1-5): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye! 📞")
        break
    else:
        print("❌ Invalid choice.")
