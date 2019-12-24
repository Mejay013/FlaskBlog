from flask import Blueprint , render_template , url_for , redirect , request
from flask_login import login_required , current_user
from .models import User , Role

main = Blueprint('main',__name__)

@main.route('/')
def index():
    user = User.query.all()
    return render_template('index.html',user = user)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name = current_user.name)



@main.route('/set/<id>')
def set(id):
    user = User.query.filter_by(id = id).first()
    role = Role.query.filter_by(id = user.role).first()
    return render_template('set.html',user = user,role = role )

@main.route('/change/<id>',methods=['POST','GET'])
def change(id):
    user = User.query.filter_by(id = id).first()
    user.query.update().values(name= request.form['new_name'])
    if request.form['new_pass']:
        user.query.update().values(password= request.form['new_password'])
    user.query.update().values(email= request.form['new_email'])
    user.query.update().values(role= request.form['new_role'])

    db.session.commit()

    return redirect(url_for('main.profile'))
