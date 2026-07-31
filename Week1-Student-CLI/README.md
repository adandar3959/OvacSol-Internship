# Student Record & Grade Management System

A command-line application for managing student records with marks and grades.

## Features

- Add, update, view, and delete student records
- Subject-wise marks management
- Automatic grade calculation
- Data persistence with JSON
- Backup functionality

## Setup

### 1. Create Virtual Environment

```bash
cd Week1-Student-CLI
python -m venv venv
```

### 2. Activate Virtual Environment

```bash
source venv/Scripts/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

## Project Structure

```
Week1-Student-CLI/
├── main.py              # Main CLI application
├── student.py           # Student class
├── file_manager.py      # File operations
├── requirements.txt     # Dependencies
└── students.json        # Data file (auto-generated)
```

## Usage

- **Option 1**: Add new student
- **Option 2**: Update student marks
- **Option 3**: View single student
- **Option 4**: View all students
- **Option 5**: Delete student
- **Option 6**: Create backup
- **Option 7**: Exit

## Grading Scale

- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

## Data Storage

All data is saved in `students.json`:

```json
{
    "101": {
        "name": "John Doe",
        "roll_number": "101",
        "marks": {
            "Math": 85.0,
            "Science": 92.0
        }
    }
}
```
