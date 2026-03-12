from flask import Blueprint, render_template, request, redirect, url_for
from app.extensions import db
from app.models.student import Student
from flask_login import login_required

students_bp = Blueprint('students', __name__)

@students_bp.route('/')
def home():
    return render_template('index.html')

@students_bp.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = int(request.form.get('student_id'))
        name = request.form.get('name')
        grades = request.form.get('grades')
        
        new_student = Student(student_id=student_id, name=name, grades=grades)
        
        db.session.add(new_student)
        db.session.commit()
        
        return redirect(url_for('students.list_students'))
    
    return render_template('add_student.html')

@students_bp.route('/students')
@login_required
def list_students():
    all_students = Student.query.all()
    return render_template('students.html', students=all_students)

@students_bp.route('/student/<int:student_id>')
def student_detail(student_id):
    student_found = Student.query.filter_by(student_id=student_id).first()
    if student_found:
        return render_template('student_detail.html', student=student_found)
    return "Student not found", 404


@students_bp.route('/student/<int:student_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_student(student_id):
    student = Student.query.filter_by(student_id=student_id).first_or_404()
    
    if request.method == 'POST':
        student.name = request.form.get('name')
        student.grades = request.form.get('grades')
        
        db.session.commit()
        
        return redirect(url_for('students.student_detail', student_id=student.student_id))
    
    return render_template('edit_student.html', student=student)


@students_bp.route('/student/<int:student_id>/delete', methods=['POST'])
@login_required
def delete_student(student_id):
    student = Student.query.filter_by(student_id=student_id).first_or_404()
    
    db.session.delete(student)
    db.session.commit()
    
    return redirect(url_for('students.list_students'))