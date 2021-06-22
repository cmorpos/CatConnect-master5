from catconnect import app
from flask import render_template, redirect, url_for, flash
from catconnect.models import Item, User
from catconnect.forms import RegisterForm
from catconnect import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/adoptionpage')
def adoption_page():
    cats = Item.query.all()
    return render_template('adoptionpage.html', cats=cats)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('adoption_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in creating a user: {err_msg}', category='danger')

    return render_template('register.html',form=form)