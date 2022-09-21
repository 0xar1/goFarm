from flask import flash, redirect, render_template, session, url_for
from flask_login import login_required,current_user
from .models import *
from flask import current_app as app



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Homepage - goFarm")



@app.route('/dashboard')
@login_required
def dashboard():
    user = current_user.uid
    # return render_template('dashboard.html', title='Dashboard')
    return render_template('/dashboard/dashboard.html',title='Dashboard - goFarm',uid = user)

@app.route('/user/<id>')
@login_required
def user(id):
    print(current_user.uid,":",id)
    print(type(current_user.uid))
    print(type(id))
    if (str(current_user.uid) != id):
        return "Unauthorized"
    else:
        temp = User.query.filter_by(uid=id).first()
    # if temp is None:
    #     return render_template('notfound.html')
        return render_template('/user/user.html',data = temp,title='Dashboard - goFarm')

@app.route('/logo')
def logo():
    # return render_template('dashboard.html', title='Dashboard')
    return render_template('/new/logo.html'  )

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")