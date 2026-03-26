from flask import Blueprint, jsonify
from app.models.student import Student

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/students', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    students_list = []
    
    for student in students:
        students_list.append({
            'id': student.id,
            'name': student.name,
            'grades': student.grades,
            'user_id': student.user_id
        })
        
    return jsonify({"students": students_list, "count": len(students_list)}), 200