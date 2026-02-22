class Student:
    def __init__(self, student_id, name, grades=None):
        self.student_id = student_id
        self.name = name
        self.grades = grades if grades is not None else []

    @property
    def gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    @classmethod
    def from_string(cls, student_str):
        student_id, name = student_str.split('-')
        return cls(int(student_id), name)

    @staticmethod
    def is_passing(gpa):
        return gpa >= 60.0
