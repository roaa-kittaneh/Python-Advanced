from flask import Flask
from config import Config
from app.extensions import db, migrate, login_manager
from app.models.user import User
from app.routes.auth import auth_bp



def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' 
    migrate.init_app(app, db)

    from app.models.student import Student
    from app.models.course import Course

    from app.routes.students import students_bp
    app.register_blueprint(students_bp)
    app.register_blueprint(auth_bp)

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))