from flask import request, flash, render_template, redirect, url_for, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user
from api.user.models import User
from app import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.post('/login')
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter(User.email==email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return 'NOT LOGGED IN' # if the user doesn't exist or password is wrong, reload the page
    login_user(user)
    return redirect(url_for('client.dashboard.user_dashboard'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' :
        new_email = request.form['email']
        new_username = request.form['username']
        new_password = request.form['password']
        password_confirmation = request.form['confirm_password']
        error = None

        if not new_email :
            error = 'Email is required'
        elif not new_username :
            error = 'Username is required'
        elif not new_password :
            error = 'Password is required'
        elif not password_confirmation :
            error = 'You must retype your password'
        elif new_password != password_confirmation :
            error = 'Passwords must match'

        hashed_password = generate_password_hash(new_password)

        print(error)

        if error is None :
            try :
                new_user = User(email=new_email, username=new_username, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()

                print('Registration Successful!')

                return redirect(url_for('login'))
            except Exception as e :
                print(e)

    return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_login'))