from app import create_app
from app.extensions import db
from app.models.student import Student
from app.models.course import Course

app = create_app()

def seed_data():

    with app.app_context():
        print("Clearing old data...")
        db.drop_all()   
        db.create_all() 

        print("Adding dummy data...")
        s1 = Student(student_id=202401, name="Ahmad Ali", grades="90,85,88")
        s2 = Student(student_id=202402, name="Sara Khaled", grades="95,92,98")
        s3 = Student(student_id=202403, name="Roaa", grades="88,90,92")

        c1 = Course(course_code="CS101", course_name="Introduction to Programming")
        c2 = Course(course_code="MATH201", course_name="Calculus I")

        db.session.add_all([s1, s2, s3, c1, c2])
        db.session.commit()

        print(" Database seeded successfully with demo data!")

if __name__ == '__main__':
    seed_data()