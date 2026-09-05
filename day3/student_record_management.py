# Student Record Management System

FILE_NAME = "students.txt"


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{student_id},{name},{age},{grade}\n")

    print("Student record added successfully!")


def view_students():
    print("\n--- Student Records ---")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("No student records found.")
                return

            for record in records:
                student_id, name, age, grade = record.strip().split(",")

                print(
                    f"ID: {student_id} | "
                    f"Name: {name} | "
                    f"Age: {age} | "
                    f"Grade: {grade}"
                )

    except FileNotFoundError:
        print("No student records found.")


def search_student():
    print("\n--- Search Student ---")

    search_id = input("Enter student ID: ")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            for record in records:
                student_id, name, age, grade = record.strip().split(",")

                if student_id == search_id:
                    print("\nStudent Found!")
                    print("ID:", student_id)
                    print("Name:", name)
                    print("Age:", age)
                    print("Grade:", grade)
                    return

            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


def main():
    while True:
        print("\n================================")
        print(" Student Record Management")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
