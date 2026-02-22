# 1. Student Class
class Student:
    def __init__(self, student_id, name, grades=None):
        self.student_id = student_id
        self.name = name
        # If no grades are passed, initialize as an empty list
        self.grades = grades if grades is not None else []

    # Using @property to calculate GPA automatically
    @property
    def gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    # Using __eq__ to define how to compare two students
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    # @classmethod: A method bound to the class itself, not the instance
    @classmethod
    def from_string(cls, student_str):
        student_id, name = student_str.split('-')
        return cls(int(student_id), name)

    # @staticmethod: A regular function that doesn't require self or cls
    @staticmethod
    def is_passing(gpa):
        return gpa >= 60.0

# 2. Course Class
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        #  the __eq__ method, Python will automatically know
        # if the student already exists based on their ID
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.name} added successfully.")
        else:
            print(f"Student {student.name} is already registered in the course!")

    # Using __iter__ to make the class iterable
    def __iter__(self):
        return iter(self.students)

    # Using __len__ to get the number of students in the course
    def __len__(self):
        return len(self.students)

# Testing the Code
if __name__ == "__main__":
    # Create students
    s1 = Student(101, "Ahmed", [85, 90, 78])
    s2 = Student(102, "Sara", [95, 88, 92])
    s3 = Student(101, "Ahmed Copy") # Student with the same ID for testing
    
    # Test (@property)
    print(f"Ahmed's GPA: {s1.gpa:.2f}")
    
    # Test comparison (__eq__)
    print(f"Is s1 the same as s3? {'Yes' if s1 == s3 else 'No'}")
    
    # Create course and add students
    python_course = Course("Advanced Python")
    python_course.add_student(s1)
    python_course.add_student(s2)
    python_course.add_student(s3) # Will be rejected because he is already registered 

    # Test iterating over students (__iter__)
    print("\nStudents registered in the course:")
    for student in python_course:
        print(f"- {student.name} (GPA: {student.gpa:.2f})")