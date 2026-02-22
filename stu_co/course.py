class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.name} has been added successfully.")
        else:
            print(f"Student {student.name} is already registered in the course!")

    def __iter__(self):
        return iter(self.students)

    def __len__(self):
        return len(self.students)
