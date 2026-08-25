from datetime import datetime
import random


# ==================================================
# PERSONAL COMMAND CENTER
# ==================================================

notes = []
tasks = []
expenses = []


# ==================================================
# HEADER
# ==================================================

def header(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


# ==================================================
# PROFILE
# ==================================================

def profile():
    header("PROFILE")

    name = input("Enter your name: ")

    print("\nYour Profile")
    print("-" * 30)
    print("Name:", name)

    input("\nPress Enter to continue...")


# ==================================================
# NOTES
# ==================================================

def notes_manager():

    while True:

        header("NOTES MANAGER")

        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Back")

        choice = input("\nChoose: ")

        if choice == "1":

            note = input("Write your note: ")

            if note:
                notes.append(note)
                print("\nNote added successfully!")

            else:
                print("\nNote cannot be empty.")

        elif choice == "2":

            print("\nYour Notes")
            print("-" * 30)

            if len(notes) == 0:
                print("No notes available.")

            else:

                for i in range(len(notes)):
                    print(i + 1, ".", notes[i])

        elif choice == "3":

            if len(notes) == 0:
                print("\nNo notes available.")

            else:

                for i in range(len(notes)):
                    print(i + 1, ".", notes[i])

                try:
                    number = int(input("\nEnter note number to delete: "))

                    if number >= 1 and number <= len(notes):
                        notes.pop(number - 1)
                        print("\nNote deleted!")

                    else:
                        print("\nInvalid number.")

                except:
                    print("\nPlease enter a number.")

        elif choice == "4":
            break

        else:
            print("\nInvalid choice.")


# ==================================================
# TASK MANAGER
# ==================================================

def task_manager():

    while True:

        header("TASK MANAGER")

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Back")

        choice = input("\nChoose: ")

        if choice == "1":

            task = input("Enter task: ")

            tasks.append({
                "task": task,
                "completed": False
            })

            print("\nTask added!")

        elif choice == "2":

            print("\nYour Tasks")
            print("-" * 30)

            if len(tasks) == 0:
                print("No tasks available.")

            else:

                for i in range(len(tasks)):

                    if tasks[i]["completed"]:
                        status = "Completed"
                    else:
                        status = "Pending"

                    print(
                        i + 1,
                        ".",
                        tasks[i]["task"],
                        "-",
                        status
                    )

        elif choice == "3":

            if len(tasks) == 0:
                print("\nNo tasks available.")

            else:

                for i in range(len(tasks)):
                    print(i + 1, ".", tasks[i]["task"])

                try:

                    number = int(input("\nEnter task number: "))

                    if number >= 1 and number <= len(tasks):

                        tasks[number - 1]["completed"] = True

                        print("\nTask completed!")

                    else:
                        print("\nInvalid number.")

                except:
                    print("\nPlease enter a number.")

        elif choice == "4":
            break

        else:
            print("\nInvalid choice.")


# ==================================================
# EXPENSE TRACKER
# ==================================================

def expense_tracker():

    while True:

        header("EXPENSE TRACKER")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Back")

        choice = input("\nChoose: ")

        if choice == "1":

            name = input("Expense name: ")

            try:
                amount = float(input("Amount: "))

                expenses.append({
                    "name": name,
                    "amount": amount
                })

                print("\nExpense added!")

            except:
                print("\nPlease enter a valid amount.")

        elif choice == "2":

            print("\nExpense History")
            print("-" * 40)

            if len(expenses) == 0:
                print("No expenses available.")

            else:

                for i in range(len(expenses)):

                    print(
                        i + 1,
                        ".",
                        expenses[i]["name"],
                        "- Rs.",
                        expenses[i]["amount"]
                    )

        elif choice == "3":

            total = 0

            for expense in expenses:
                total = total + expense["amount"]

            print("\nTotal Expenses: Rs.", total)

        elif choice == "4":
            break

        else:
            print("\nInvalid choice.")


# ==================================================
# CALCULATOR
# ==================================================

def calculator():

    header("CALCULATOR")

    try:

        number1 = float(input("Enter first number: "))
        operator = input("Enter operator (+ - * /): ")
        number2 = float(input("Enter second number: "))

        if operator == "+":
            result = number1 + number2

        elif operator == "-":
            result = number1 - number2

        elif operator == "*":
            result = number1 * number2

        elif operator == "/":

            if number2 == 0:
                print("\nCannot divide by zero.")
                return

            result = number1 / number2

        else:
            print("\nInvalid operator.")
            return

        print("\nResult:", result)

    except:
        print("\nInvalid input.")


# ==================================================
# PASSWORD GENERATOR
# ==================================================

def password_generator():

    header("PASSWORD GENERATOR")

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    try:
        length = int(input("Enter password length: "))

        password = ""

        for i in range(length):
            password = password + random.choice(characters)

        print("\nGenerated Password:")
        print(password)

    except:
        print("\nPlease enter a number.")


# ==================================================
# DATE & TIME
# ==================================================

def date_time():

    header("DATE & TIME")

    now = datetime.now()

    print("Date:", now.strftime("%d-%m-%Y"))
    print("Time:", now.strftime("%I:%M:%S %p"))
    print("Day :", now.strftime("%A"))


# ==================================================
# STATISTICS
# ==================================================

def statistics():

    header("PERSONAL STATISTICS")

    total_tasks = len(tasks)
    completed_tasks = 0

    for task in tasks:

        if task["completed"]:
            completed_tasks += 1

    total_expenses = 0

    for expense in expenses:
        total_expenses += expense["amount"]

    print("Total Notes:", len(notes))
    print("Total Tasks:", total_tasks)
    print("Completed Tasks:", completed_tasks)
    print("Total Expenses: Rs.", total_expenses)

    if total_tasks > 0:

        percentage = (completed_tasks / total_tasks) * 100

        print("Task Completion:", round(percentage, 2), "%")


# ==================================================
# MAIN MENU
# ==================================================

def main():

    name = input("Enter your name: ")

    while True:

        header("PERSONAL COMMAND CENTER")

        print("Welcome,", name)

        print("""
1. Profile
2. Notes Manager
3. Task Manager
4. Expense Tracker
5. Calculator
6. Password Generator
7. Date & Time
8. Statistics
0. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            profile()

        elif choice == "2":
            notes_manager()

        elif choice == "3":
            task_manager()

        elif choice == "4":
            expense_tracker()

        elif choice == "5":
            calculator()

        elif choice == "6":
            password_generator()

        elif choice == "7":
            date_time()

        elif choice == "8":
            statistics()

        elif choice == "0":

            print("\nThank you for using Personal Command Center!")
            break

        else:
            print("\nInvalid choice.")


# ==================================================
# START PROGRAM
# ==================================================

main()