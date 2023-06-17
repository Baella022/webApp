# views.py
import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from website.models import User, ContactMessage
from website import db, login_manager

views = Blueprint('views', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@views.route('/')
def home():
    users = User.get_all()  # Fetch all users from the database
    messages = ContactMessage.get_all()  # Fetch all contact messages from the database

    return render_template("home.html", users=users, messages=messages)

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        contact_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(contact_message)
        db.session.commit()
        flash('Your message has been sent successfully!', 'success')

        # Write data to the file
        file_path = os.path.join(os.getcwd(), 'data.txt')
        with open(file_path, 'a') as file:
            file.write(f'Name: {name}, Email: {email}, Message: {message}\n')

        return redirect(url_for('views.home'))  # Redirect to the home page after sending the comment

    return render_template("contact.html", user=current_user)


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@views.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.logout_page'))

@views.route('/logout-page')
def logout_page():
    return render_template('logout.html')

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.login'))  # Redirect to the login page after successful signup

        # Additional password length validation
        if len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')

    return render_template("signup.html")



@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/grade3')
def grade3():
    return render_template("grade3.html")

@views.route('/grade4')
def grade4():
    return render_template('grade4.html')

@views.route('/grade5')
def grade5():
    return render_template('grade5.html')

@views.route('/grade6')
def grade6():
    return render_template('grade6.html')

@views.route('/grade7')
def grade7():
    return render_template('grade7.html')

@views.route('/grade8')
def grade8():
    return render_template('grade8.html')
