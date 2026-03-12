from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.extensions import db
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('the username is already taken.', 'danger')
            return redirect(url_for('auth.register'))

        new_user = User(username=username)
        new_user.set_password(password) 

        db.session.add(new_user)
        db.session.commit()

        flash('account created successfully! you can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user) 
            flash('logged in successfully!', 'success')
            return redirect(url_for('students.list_students')) 
        else:
            flash('the username or password is incorrect.', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
@login_required 
def logout():
    logout_user() 
    flash('logged out successfully!', 'info')
    return redirect(url_for('auth.login'))