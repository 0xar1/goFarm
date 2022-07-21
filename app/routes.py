from flask import flash, redirect, render_template, session, url_for
from flask_mysqldb import MySQL

from app import app
from app.forms import LoginForm, RegisterForm




mysql = MySQL(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Homepage - goFarm")



@app.route('/dashboard')
def dashboard():
    # return render_template('dashboard.html', title='Dashboard')
    return render_template('/dashboard/dashboard.html',title='Dashboard - goFarm')

@app.route('/logo')
def logo():
    # return render_template('dashboard.html', title='Dashboard')
    return render_template('/new/logo.html'  )
