from flask import Flask, render_template, request, redirect, url_for
from stu_co.student import Student

app = Flask(__name__)

registered_students = []

# 1.home page
@app.route('/')
def home():
    return render_template('index.html')

# 2. صفحة التسجيل 
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_id = int(request.form.get('student_id'))
        name = request.form.get('name')
        grades_str = request.form.get('grades')
        
        grades = [int(g.strip()) for g in grades_str.split(',')] if grades_str else []
        new_student = Student(student_id, name, grades)
        registered_students.append(new_student)
        
        return redirect(url_for('list_students'))
    
    return render_template('register.html')

# 3. صفحة عرض كل الطلاب
@app.route('/students')
def list_students():
    return render_template('students.html', students=registered_students)

@app.route('/student/<int:student_id>')
def student_detail(student_id):
    student_found = next((s for s in registered_students if s.student_id == student_id), None)
    
    if student_found:
        return render_template('student_detail.html', student=student_found)
    return "Student not found", 404

if __name__ == '__main__':
    app.run(debug=True)