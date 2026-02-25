from flask import Flask, render_template, request, redirect, url_for
#كلاس الطالب في التاسك الأول!
from stu_co.student import Student

app = Flask(__name__)

registered_students = []

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_id = int(request.form.get('student_id'))
        name = request.form.get('name')
        grades_str = request.form.get('grades')
        
        if grades_str:
            grades = [int(g.strip()) for g in grades_str.split(',')]
        else:
            grades = []

        new_student = Student(student_id, name, grades)
        registered_students.append(new_student)

        return redirect(url_for('list_students'))
    
    return render_template('register.html')

# المسار الثاني: عرض جميع الطلاب
@app.route('/students')
def list_students():
    return render_template('students.html', students=registered_students)

if __name__ == '__main__':
    app.run(debug=True)