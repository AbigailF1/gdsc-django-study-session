studentDatabase = {}

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    studentDatabase[name] = {'Age': age, 'Grade': grade}
    print(f"Student {name} added to the database.")

def view_student():
    name = input("Enter student name to view details: ")
    if name in studentDatabase:
        print(f"Details for {name}: {studentDatabase[name]}")
    else:
        print(f"Student {name} not found in the database.")

def list_all_students():
    print("List of all students:")
    for name, details in studentDatabase.items():
        print(f"{name}: {details}")

def update_student_information():
    name = input("Enter student name to update information: ")
    if name in studentDatabase:
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")

        studentDatabase[name]['Age'] = age
        studentDatabase[name]['Grade'] = grade
        print(f"Information for {name} updated.")
    else:
        print(f"Student {name} not found in the database.")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in studentDatabase:
        del studentDatabase[name]
        print(f"Student {name} deleted from the database.")
    else:
        print(f"Student {name} not found in the database.")

def main():
    while True:
        print("\nStudent Database Menu:")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            list_all_students()
        elif choice == '4':
            update_student_information()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
