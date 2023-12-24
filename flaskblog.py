from flask import Flask, render_template
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


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
