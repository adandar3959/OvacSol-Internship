import json
import os
from student import Student

DATA_FILE = 'students.json'

def load_students():
    students = {}
    
    try:
        if not os.path.exists(DATA_FILE):
            print(f"No existing data file found. Starting fresh.")
            return students
        
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            
            for roll_number, student_data in data.items():
                students[roll_number] = Student.from_dict(student_data)
            
            print(f"Loaded {len(students)} student(s)")
    
    except json.JSONDecodeError as e:
        print(f"Error: File is corrupted. Starting fresh.")
    except PermissionError:
        print(f"Error: Can't read file (permission denied)")
    except Exception as e:
        print(f"Error loading data: {e}")
    
    return students


def save_students(students):
    try:
        data = {}
        for roll_number, student in students.items():
            data[roll_number] = student.to_dict()
        
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Data saved successfully!")
        return True
    
    except PermissionError:
        print(f"Error: Can't save file (permission denied)")
        return False
    except IOError as e:
        print(f"Error: Failed to save file. {e}")
        return False
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def create_backup():
    try:
        if os.path.exists(DATA_FILE):
            backup_file = DATA_FILE + '.backup'
            
            with open(DATA_FILE, 'r') as source:
                with open(backup_file, 'w') as dest:
                    dest.write(source.read())
            
            print(f"Backup created: {backup_file}")
            return True
        else:
            print("No file to backup")
            return False
    
    except Exception as e:
        print(f"Error creating backup: {e}")
        return False
