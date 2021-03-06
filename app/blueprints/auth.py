from flask import Blueprint,redirect,url_for, render_template,flash
from flask_login import current_user,login_user,logout_user
from ..models import db,User
from flask import current_app as app
from ..forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__,template_folder='authTemplate')


@auth.route('/register', methods = ['GET', 'POST'])
def signup():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        print('\n\nDone\n\n')
        user_exist = User.query.filter_by(email=form.email.data).first()
        if user_exist is None:
            user = User(
                full_name = form.fullname.data,
                email = form.email.data,
                )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('User with the same email exist')
    return render_template('signup.html', title='SignIn - goFarm', form=form)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        print(user)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('dashboard'))

    
    # if form.validate_on_submit():
    #     email = form.email.data

    #     cur = mysql.connection.cursor()

    #     temp = cur.execute('SELECT password from user WHERE mail=%s', (email,))  
    #     password = cur.fetchone()

    #     cur.close
        
    #     verified = decrypt(str(form.password.data), str(password[0])) 
    #     print(password[0])
    #     if verified == True:
    #         flash('You are now registered and may login.', 'success')
    #         return redirect(url_for('dashboard'))
    #     else:
    #         return "Passwords does not match"
        
    return render_template('login.html', title='SignIn - goFarm', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))








   # if form.validate_on_submit():
    #     name = form.fullname.data
    #     email = form.email.data
    #     password = str(encrypt(form.password.data))
    #     verified = 0
    #     cur = mysql.connection.cursor() 
    #     cur.execute("SELECT mail FROM user where mail = %s",(email,))
    #     maillist = cur.fetchone()
    #     # print(maillist)
        
        
    #     # if maillist[0] == email:
    #     cur.execute("INSERT INTO user(full_name, mail, password, verified) VALUES(%s, %s, %s,%s)", (name, email, password, verified))
    #     mysql.connection.commit()
    #     cur.close
    #     flash('You are now registered and may login.', 'success')
    #     # redirect(url_for('dashboard'))

    #     return redirect(url_for('login'))