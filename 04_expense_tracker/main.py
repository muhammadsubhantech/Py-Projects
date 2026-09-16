# Simple Expense Tracker
# Student Level Pure Python Project

expenses = []

def show_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Spent")
    print("4. Exit")

def add_expense():
    try:
        amount = float(input("Enter amount (Rs): "))
        category = input("Category (Food/Travel/Shopping/Other): ").title()
        note = input("Note (optional): ")

        expenses.append({
            "amount": amount,
            "category": category,
            "note": note
        })
        print("✅ Expense added!")
    except ValueError:
        print("❌ Please enter a valid amount.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n----- All Expenses -----")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. Rs {e['amount']} | {e['category']} | {e['note']}")

def show_total():
    if not expenses:
        print("No expenses yet.")
        return

    total = sum(e["amount"] for e in expenses)
    print(f"\n💰 Total Spent: Rs {total:.2f}")

    # Category wise
    category_total = {}
    for e in expenses:
        cat = e["category"]
        category_total[cat] = category_total.get(cat, 0) + e["amount"]

    print("\n--- Category Wise ---")
    for cat, amount in category_total.items():
        print(f"{cat}: Rs {amount:.2f}")

while True:
    show_menu()
    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Bye! Track your money wisely 💰")
        break
    else:
        print("❌ Invalid choice.")
