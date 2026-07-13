# Student Attendance Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    students[roll] = {
        "Name": name,
        "Attendance": []
    }
    print("Student added successfully!")

def mark_attendance():
    if not students:
        print("No students available.")
        return

    date = input("Enter Date (DD-MM-YYYY): ")

    for roll, details in students.items():
        print(f"\nRoll No: {roll}")
        print(f"Name: {details['Name']}")
        status = input("Present (P) / Absent (A): ").upper()

        while status not in ["P", "A"]:
            status = input("Invalid! Enter P or A: ").upper()

        details["Attendance"].append((date, status))

    print("\nAttendance marked successfully!")

def view_attendance():
    if not students:
        print("No records found.")
        return

    print("\nAttendance Records")
    print("-" * 40)

    for roll, details in students.items():
        print(f"Roll No : {roll}")
        print(f"Name    : {details['Name']}")

        if details["Attendance"]:
            for record in details["Attendance"]:
                print(f"Date: {record[0]}  Status: {record[1]}")
        else:
            print("No attendance recorded.")

        print("-" * 40)

def search_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        details = students[roll]
        print(f"\nName: {details['Name']}")
        print("Attendance:")

        if details["Attendance"]:
            for record in details["Attendance"]:
                print(f"{record[0]} - {record[1]}")
        else:
            print("No attendance records.")
    else:
        print("Student not found.")

while True:
    print("\n===== Student Attendance Management System =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Search Student Attendance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_attendance()
    elif choice == "4":
        search_student()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")
