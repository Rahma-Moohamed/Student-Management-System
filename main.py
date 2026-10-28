
import json
import os


class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def display_info(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Grade:", self.grade)

        if self.grade >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }


class StudentManagement:
    def __init__(self):
        self.students = []
        self.file_name = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "students.json"
        )
        self.load_students()

    def load_students(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)

            for item in data:
                student = Student(
                    item["student_id"],
                    item["name"],
                    item["grade"]
                )
                self.students.append(student)

            print("Student data loaded successfully!")

        except FileNotFoundError:
            print("No saved data found. Starting with an empty list.")

        except (json.JSONDecodeError, KeyError, TypeError):
            print("The data file is invalid. Starting with an empty list.")
            self.students = []

    def save_students(self):
        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_student(self):
        student_id = input("Enter student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty!")
            return

        for student in self.students:
            if student.student_id == student_id:
                print("This ID already exists!")
                return

        name = input("Enter student name: ").strip()

        if not name:
            print("Student name cannot be empty!")
            return

        try:
            grade = float(input("Enter student grade: "))
        except ValueError:
            print("Grade must be a number!")
            return

        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100!")
            return

        student = Student(student_id, name, grade)
        self.students.append(student)
        self.save_students()

        print("Student added and saved successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found.")
            return

        for student in self.students:
            print("--------------------")
            student.display_info()

    def search_student(self):
        student_id = input("Enter student ID to search: ").strip()

        for student in self.students:
            if student.student_id == student_id:
                print("Student found:")
                student.display_info()
                return

        print("Student not found.")

    def update_student(self):
        student_id = input("Enter student ID to update: ").strip()

        for student in self.students:
            if student.student_id == student_id:
                new_name = input("Enter new name: ").strip()

                if not new_name:
                    print("Student name cannot be empty!")
                    return

                try:
                    new_grade = float(input("Enter new grade: "))
                except ValueError:
                    print("Grade must be a number!")
                    return

                if new_grade < 0 or new_grade > 100:
                    print("Grade must be between 0 and 100!")
                    return

                student.name = new_name
                student.grade = new_grade

                self.save_students()
                print("Student updated and saved successfully!")
                return

        print("Student not found.")

    def delete_student(self):
        student_id = input("Enter student ID to delete: ").strip()

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully!")
                return

        print("Student not found.")


management = StudentManagement()

while True:
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        management.add_student()

    elif choice == "2":
        management.view_students()

    elif choice == "3":
        management.search_student()

    elif choice == "4":
        management.update_student()

    elif choice == "5":
        management.delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again")
