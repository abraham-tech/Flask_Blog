from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
