from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '78c4ce8924cc88d75128ce708249db51'

posts = [
    {
        'author': 'Alice',
        'title': 'First Steps in Python',
        'content': 'This is a blog post about getting started with Python.',
        'date_posted': 'May 15, 2023'
    },
    {
        'author': 'Bob',
        'title': 'Understanding Decorators',
        'content': 'This is a blog post about Python decorators.',
        'date_posted': 'May 20, 2023'
    },
    {
        'author': 'Charlie',
        'title': 'Exploring Flask',
        'content': 'This blog post explores the Flask web framework.',
        'date_posted': 'May 23, 2023'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
