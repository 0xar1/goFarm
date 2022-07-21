from flask import Blueprint,redirect,url_for, render_template,flash
from flask_mysqldb import MySQL
from .. import app
from ..forms import LoginForm, RegisterForm
from ..passwordhasher import decrypt, encrypt
auth = Blueprint('auth', __name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'passwordroot69'
app.config['MYSQL_DB'] = 'app'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)


@auth.route('/register', methods = ['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.fullname.data
        email = form.email.data
        password = str(encrypt(form.password.data))
        verified = 0
        cur = mysql.connection.cursor() 
        cur.execute("SELECT mail FROM user where mail = %s",(email,))
        maillist = cur.fetchone()
        # print(maillist)
        
        
        # if maillist[0] == email:
        cur.execute("INSERT INTO user(full_name, mail, password, verified) VALUES(%s, %s, %s,%s)", (name, email, password, verified))
        mysql.connection.commit()
        cur.close
        flash('You are now registered and may login.', 'success')
        # redirect(url_for('dashboard'))

        return redirect(url_for('login'))
        
    return render_template('register.html', title='SignIn - goFarm', form=form)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data

        cur = mysql.connection.cursor()

        temp = cur.execute('SELECT password from user WHERE mail=%s', (email,))  
        password = cur.fetchone()

        cur.close
        
        verified = decrypt(str(form.password.data), str(password[0])) 
        print(password[0])
        if verified == True:
            flash('You are now registered and may login.', 'success')
            return redirect(url_for('dashboard'))
        else:
            return "Passwords does not match"
        
    return render_template('login.html', title='SignIn - goFarm', form=form)
  