from stu_co.student import Student
from stu_co.course import Course

if __name__ == "__main__":
    # Create students
    s1 = Student(101, "Ahmed", [85, 90, 78])
    s2 = Student(102, "Sara", [95, 88, 92])
    s3 = Student(101, "Ahmed Copy", [85, 90, 78]) 
    
    print(f"Ahmed's GPA: {s1.gpa}")
    print(f"Is s1 the same as s3? {'Yes' if s1 == s3 else 'No'}")
    
    # Create course and add students
    python_course = Course("Advanced Python")
    python_course.add_student(s1)
    python_course.add_student(s2)
    python_course.add_student(s3) 

    print("\nRegistered students in the course:")
    for student in python_course:
        print(f"- {student.name} (GPA: {student.gpa:.2f})")