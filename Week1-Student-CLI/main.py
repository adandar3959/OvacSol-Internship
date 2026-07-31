from student import Student
from file_manager import load_students, save_students, create_backup
from tabulate import tabulate


def display_menu():

    print("\n" + "="*50)
    print("  STUDENT RECORD & GRADE MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add New Student")
    print("2. Update Student Marks")
    print("3. View Single Student")
    print("4. View All Students")
    print("5. Delete Student")
    print("6. Create Backup")
    print("7. Exit")
    print("="*50)


def add_student(students):
    print("\n--- Add New Student ---")
    
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return
        
        roll_number = input("Enter roll number: ").strip()
        if not roll_number:
            print("Error: Roll number cannot be empty.")
            return
        
        if roll_number in students:
            print(f"Error: Student with roll number {roll_number} already exists.")
            return
        
        student = Student(name, roll_number)
        add_marks = input("Do you want to add marks now? (y/n): ").lower()
        
        if add_marks == 'y':
            add_marks_to_student(student)
        
        students[roll_number] = student
        print(f"✓ Student {name} added successfully!")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error adding student: {e}")


def add_marks_to_student(student):
    print("\nEnter subject and marks (or 'done' to finish):")
    
    while True:
        try:
            subject = input("  Subject name (or 'done'): ").strip()
            
            if subject.lower() == 'done':
                break
            
            if not subject:
                print("  Error: Subject name cannot be empty.")
                continue
            
            mark_input = input(f"  Marks for {subject}: ").strip()
            mark = float(mark_input)
            
            if mark < 0 or mark > 100:
                print("  Error: Marks must be between 0 and 100.")
                continue
            
            student.add_or_update_marks(subject, mark)
            print(f"  ✓ Added {subject}: {mark}")
            
        except ValueError:
            print("  Error: Invalid marks. Please enter a number.")
        except KeyboardInterrupt:
            print("\nStopping mark entry.")
            break


def update_marks(students):
    print("\n--- Update Student Marks ---")
    
    try:
        roll_number = input("Enter roll number: ").strip()
        
        if roll_number not in students:
            print(f"Error: No student found with roll number {roll_number}")
            return
        
        student = students[roll_number]
        print(f"Updating marks for: {student.name}")
        
        if student.marks:
            print("\nExisting marks:")
            for subject, mark in student.marks.items():
                print(f"  {subject}: {mark}")
        
        add_marks_to_student(student)
        print("✓ Marks updated successfully!")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error updating marks: {e}")


def view_student(students):
    print("\n--- View Student ---")
    
    try:
        roll_number = input("Enter roll number: ").strip()
        
        if roll_number not in students:
            print(f"Error: No student found with roll number {roll_number}")
            return
        
        student = students[roll_number]
        
        print(f"Name: {student.name}")
        print(f"Roll Number: {student.roll_number}")

        if student.marks:
            marks_data = [[subject, mark] for subject, mark in student.marks.items()]
            print("\nMarks:")
            print(tabulate(marks_data, headers=['Subject', 'Marks'], tablefmt='grid'))
            
            print(f"\nTotal Marks: {student.calculate_total():.2f}")
            print(f"Average Marks: {student.calculate_average():.2f}")
            print(f"Grade: {student.calculate_grade()}")
        else:
            print("\nNo marks recorded yet.")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error viewing student: {e}")


def view_all_students(students):
    print("\n--- All Students ---")
    
    if not students:
        print("No students in the system yet.")
        return
    
    try:
        table_data = []
        
        for roll_number, student in students.items():
            table_data.append([
                student.roll_number,
                student.name,
                len(student.marks),
                f"{student.calculate_total():.2f}" if student.marks else "N/A",
                f"{student.calculate_average():.2f}" if student.marks else "N/A",
                student.calculate_grade() if student.marks else "N/A"
            ])
        
        headers = ['Roll No.', 'Name', 'Subjects', 'Total', 'Average', 'Grade']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))
        print(f"\nTotal Students: {len(students)}")
        
    except Exception as e:
        print(f"Error displaying students: {e}")


def delete_student(students):
    print("\n--- Delete Student ---")
    
    try:
        roll_number = input("Enter roll number: ").strip()
        
        if roll_number not in students:
            print(f"Error: No student found with roll number {roll_number}")
            return
        
        student = students[roll_number]
        confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ").lower()
        
        if confirm == 'y':
            del students[roll_number]
            print(f"✓ Student {student.name} deleted successfully!")
        else:
            print("Deletion cancelled.")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error deleting student: {e}")


def main():
    print("\nWelcome to Student Record & Grade Management System!")
    
    students = load_students()
    
    while True:
        try:
            display_menu()
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == '1':
                add_student(students)
            elif choice == '2':
                update_marks(students)
            elif choice == '3':
                view_student(students)
            elif choice == '4':
                view_all_students(students)
            elif choice == '5':
                delete_student(students)
            elif choice == '6':
                create_backup()
            elif choice == '7':
                print("\nSaving data...")
                save_students(students)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
            
            if choice in ['1', '2', '5']:
                save_students(students)
        
        except KeyboardInterrupt:
            print("\n\nExiting... Saving data...")
            save_students(students)
            print("Goodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
