from app.extensions import db

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    grades = db.Column(db.String(200), default="")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @property
    def gpa(self):
        if not self.grades:
            return 0.0
        grades_list = [int(g.strip()) for g in self.grades.split(',')]
        return sum(grades_list) / len(grades_list)
    
    
    @property
    def is_passing(self):
        return self.gpa >= 60  
    
