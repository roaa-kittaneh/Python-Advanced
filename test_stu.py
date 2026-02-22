from stu_co.student import Student

def test_student_gpa():
    # إنشاء طالب لتيست
    s = Student(1, "Test Student", [90, 80, 100])
    assert hasattr(s, 'gpa'), "Student object must have a 'gpa' attribute"
    assert abs(s.gpa - 90.0) < 1e-6

def test_student_equality():
    s1 = Student(1, "Ali", [85, 90, 80])
    s2 = Student(1, "Omar", [70, 75, 80])
    assert s1 == s2