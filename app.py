from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager ,UserMixin



db = SQLAlchemy()

app = Flask(__name__)
application = app

app.config["SECRET_KEY"] = '_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db.init_app(app)
from .models import User

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)



# from flask import Flask ,request, render_template , url_for , redirect
# from collections import Counter
# import re
# app = Flask(__name__)
# application = app

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/profile')
# def profile():
#     return render_template('profile.html')

# @app.route('/login',methods=['POST','GET'] ) 
# def login():
#     return render_template('login.html')
# @app.route('/singup' , methods=["POST",'GET'])
# def signup():
#     return render_template('signup.html')
# @app.route('/logout')
# def logout():
#     #some pass
#     return redirect(url_for('index'))