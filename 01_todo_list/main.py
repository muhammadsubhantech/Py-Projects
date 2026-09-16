# Simple To-Do List App
# Student Level Pure Python Project

tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("✅ Task added!")
    else:
        print("❌ Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['task']}")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("✅ Task marked as done!")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"🗑️ Deleted: {removed['task']}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a number.")

while True:
    show_menu()
    choice = input("Choose option (1-5): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice. Try again.")
