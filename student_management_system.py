students = []

def add_student(name, student_id):
    students.append({"name": name, "student_id": student_id})
    print(f"Student {name} with ID {student_id} added successfully.")

def view_students():
    if not students:
        print("No students in the system.")
    else:
        for student in students:
            print(f"Name: {student['name']}, ID: {student['student_id']}")

def search_student(search_term):
    found_students = [student for student in students if search_term.lower() in student['name'].lower() or search_term == student['student_id']]
    if found_students:
        print("Matching students found:")
        for student in found_students:
            print(f"Name: {student['name']}, ID: {student['student_id']}")
    else:
        print(f"No students found for search term: {search_term}")

def delete_student(student_id):
    global students
    students = [student for student in students if student['student_id'] != student_id]
    print(f"Student with ID {student_id} deleted from the system.")

def update_student(student_id):
    for student in students:
        if student['student_id'] == student_id:
            new_name = input("Enter new name: ")
            new_id = input("Enter new student ID: ")
            student['name'] = new_name
            student['student_id'] = new_id
            print(f"Student with ID {student_id} has been updated.")
            return
    print(f"Student with ID {student_id} not found in the system.")

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student (by name or ID)")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter the student's name: ")
            student_id = input("Enter the student's ID: ")
            add_student(name, student_id)
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_term = input("Enter the student's name or ID to search: ")
            search_student(search_term)
        elif choice == '4':
            student_id = input("Enter the student's ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            student_id = input("Enter the student's ID to update: ")
            update_student(student_id)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
