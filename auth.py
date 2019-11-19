from flask import Blueprint , render_template , redirect , url_for , request , flash 
from werkzeug.security import generate_password_hash , check_password_hash
from .app import db
from flask_login import login_required , current_user , login_user
from .models import User
auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email = email).first()
        if not user or not check_password_hash(user.password, password):
            flash ('Please check your login details')
            return redirect(url_for('auth.login'))
        
        login_user(user)
        return redirect(url_for('main.profile'))

    return render_template('login.html')


@auth.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email adress already exists')
            return redirect(url_for('auth.signup'))

        new_user = User(email=email , name= name , password=generate_password_hash(password,method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.profile'))
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

