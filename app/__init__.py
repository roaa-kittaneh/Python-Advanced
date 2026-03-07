from flask import Flask
from config import Config
from app.extensions import db, migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.student import Student
    from app.models.course import Course

    from app.routes.students import students_bp
    app.register_blueprint(students_bp)

    return app