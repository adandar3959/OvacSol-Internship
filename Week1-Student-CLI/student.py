class Student:
    
    def __init__(self, name, roll_number, marks=None):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks if marks is not None else {}
    
    def add_or_update_marks(self, subject, mark):
        self.marks[subject] = mark
    
    def calculate_total(self):
        return sum(self.marks.values())
    
    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return self.calculate_total() / len(self.marks)
    
    def calculate_grade(self):
        average = self.calculate_average()
        
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    def to_dict(self):
        return {
            'name': self.name,
            'roll_number': self.roll_number,
            'marks': self.marks
        }
    
    @staticmethod
    def from_dict(data):
        return Student(
            name=data['name'],
            roll_number=data['roll_number'],
            marks=data.get('marks', {})
        )
    
    def __str__(self):
        return f"Student({self.name}, Roll: {self.roll_number})"
