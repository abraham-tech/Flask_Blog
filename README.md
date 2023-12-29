# Flask Blog Application

This is a Flask blog application which includes features such as user registration, login, updating profiles with profile pictures, creating, updating and deleting blog posts.

## Features

- User Registration
- User Login & Logout
- User Profile Update
- Create, Update, Delete Posts
- Password Reset via Email

## Installation

Please ensure that all dependencies are installed. This application requires the following Python packages:
- flask
- flask_login
- flask_mail
- flask_bootstrap (If used)
- ... (Any other package dependencies specific to this project)

You can install these packages using pip:

## Usage

The blog application can be started by running `app.py`.

The application includes several routes:

- `/register`: User registration
- `/login`: User login
- `/logout`: User logout
- `/account`: User profile update
- `/post/new`: New post creation
- `/post/<int:post_id>`: Display a specific post
- `/post/<int:post_id>/update`: Update a specific post
- `/post/<int:post_id>/delete`: Delete a specific post
- `/user/<string:username>`: Display all posts from a specific user

## License

[MIT](https://choosealicense.com/licenses/mit/)