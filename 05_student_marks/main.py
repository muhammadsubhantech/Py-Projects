# Student Marks Management System
# Student Level Pure Python Project

students = []

def show_menu():
    print("\n===== STUDENT MARKS SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Show Topper")
    print("5. Exit")

def add_student():
    name = input("Student Name: ").strip()
    try:
        marks = float(input("Marks (out of 100): "))
        if marks < 0 or marks > 100:
            print("❌ Marks should be between 0 and 100.")
            return

        students.append({"name": name, "marks": marks})
        print("✅ Student added!")
    except ValueError:
        print("❌ Please enter valid marks.")

def view_students():
    if not students:
        print("No students added yet.")
        return

    print("\n----- Student List -----")
    print(f"{'Name':<20} {'Marks':<10} {'Grade'}")
    print("-" * 40)
    for s in students:
        grade = get_grade(s["marks"])
        print(f"{s['name']:<20} {s['marks']:<10} {grade}")

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def search_student():
    name = input("Enter name to search: ").strip().lower()
    found = False
    for s in students:
        if name in s["name"].lower():
            print(f"Found → {s['name']} : {s['marks']} marks ({get_grade(s['marks'])})")
            found = True
    if not found:
        print("❌ Student not found.")

def show_topper():
    if not students:
        print("No students added yet.")
        return

    topper = max(students, key=lambda x: x["marks"])
    print(f"\n🏆 Topper: {topper['name']} with {topper['marks']} marks")

while True:
    show_menu()
    choice = input("Choose (1-5): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        show_topper()
    elif choice == "5":
        print("Goodbye! 📚")
        break
    else:
        print("❌ Invalid choice.")
