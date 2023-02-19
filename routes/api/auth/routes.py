from flask import request, flash, render_template, redirect, url_for, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user
from models.user.User import User
from app import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.post('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    print(password)
    user = User.query.filter(User.username==username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return 'NOT LOGGED IN' # if the user doesn't exist or password is wrong, reload the page
    login_user(user)
    return redirect(url_for('client.dashboard.user_dashboard'))

@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST' :
        new_email = request.form['email']
        new_username = request.form['username']
        new_password = request.form['password']
        password_confirmation = request.form['confirm_password']
        error = None
        errors = []
        form_data = {}

        if not new_email :
            error = 'Email is required'
            errors.append(error)
        else:
            form_data['email'] = new_email

        if not new_username :
            error = 'Username is required'
            errors.append(error)
        else:
            form_data['username'] = new_username

        if not new_password :
            error = 'Password is required'
            errors.append(error)
        else:
            form_data['password'] = new_password

        if not password_confirmation :
            error = 'You must retype your password'
            errors.append(error)
        else:
            form_data['confirm_password'] = password_confirmation

        hashed_password = generate_password_hash(new_password)

        if db.session.query(User.id).filter_by(username=new_username).first():
            errors.append('Username already is use')

        if db.session.query(User.id).filter_by(email=new_email).first():
            errors.append('Email already is use')

        if error is None :
            try :
                new_user = User(email=new_email, username=new_username, password=hashed_password, user_avatar_id=1)
                db.session.add(new_user)
                db.session.commit()

                print('Registration Successful!')

                return redirect(url_for('client.auth.get_login'))
            except Exception as e :
                print(e)
        print(errors)
        return render_template('register.html',errors=errors, form_data=form_data)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('client.auth.get_login'))