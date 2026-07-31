# Week 1 Topics Implementation

This document shows where each Python concept from Week 1 was used in the Student Management System project.

## 1. Variables and Data Types
- **student.py**: `name` (str), `roll_number` (str), `marks` (dict)
- **main.py**: `choice` (str), `mark` (float), `table_data` (list)
- **file_manager.py**: `DATA_FILE` (str), `students` (dict)

## 2. Loops
- **While loop**: `main.py` line 243 - Main menu runs continuously until exit
- **For loops**: Used throughout to iterate over student dictionaries and display data
  - `file_manager.py` line 30 - Loading students from JSON
  - `main.py` line 229 - Preparing table data for display

## 3. Functions
Created modular, reusable functions across all files:
- **student.py**: `calculate_total()`, `calculate_average()`, `calculate_grade()`
- **file_manager.py**: `load_students()`, `save_students()`, `create_backup()`
- **main.py**: `add_student()`, `update_marks()`, `view_student()`, `delete_student()`

## 4. Object-Oriented Programming (OOP)
- **student.py**: Complete `Student` class with:
  - Constructor: `__init__(name, roll_number, marks)`
  - Methods: Grade calculations, mark updates
  - Static method: `from_dict()` for object creation from JSON
  - Demonstrates encapsulation and abstraction

## 5. File Handling
- **file_manager.py**: 
  - Reading: `with open(DATA_FILE, 'r')` to load student data
  - Writing: `with open(DATA_FILE, 'w')` to save records
  - Uses JSON format for structured data storage
  - Context managers ensure proper file closing

## 6. Exception Handling
Try/except blocks protect against errors:
- **JSONDecodeError**: Invalid JSON file format
- **ValueError**: Invalid number input for marks
- **PermissionError**: File access denied
- **KeyboardInterrupt**: User cancellation (Ctrl+C)
- Implemented in all user input and file operations

## 7. Modules
- **Built-in**: `json` (serialization), `os` (file operations)
- **Third-party**: `tabulate` (pretty table display)
- **Custom**: Three separate modules for organization:
  - `student.py` - Business logic
  - `file_manager.py` - Data layer
  - `main.py` - User interface

## 8. Virtual Environment
- Setup instructions in README.md
- Isolates project dependencies from system Python
- Created with: `python -m venv venv`

## 9. Pip and Package Management
- **requirements.txt**: Lists `tabulate==0.9.0`
- Installed with: `pip install -r requirements.txt`
- Ensures consistent environment across systems

---