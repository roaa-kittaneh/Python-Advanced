from flask import Blueprint, render_template, request, redirect, url_for
from app.models.course import Course
from app.extensions import db

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses', methods=['GET'])
def courses():
    all_courses = Course.query.all()
    return render_template('courses.html', courses=all_courses)

@course_bp.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_name = request.form['course_name']
        course_code = request.form['course_code']
        
        new_course = Course(course_name=course_name, course_code=course_code)
        db.session.add(new_course)
        db.session.commit()
        
        return redirect(url_for('course.courses'))
        
    return render_template('add_course.html')


@course_bp.route('/edit_course/<int:course_id>', methods=['GET', 'POST'])
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    
    if request.method == 'POST':
        course.course_name = request.form['course_name']
        course.course_code = request.form['course_code']
        
        db.session.commit()
        return redirect(url_for('course.courses'))
    
    return render_template('edit_course.html', course=course)


@course_bp.route('/delete_course/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    
    return redirect(url_for('course.courses'))