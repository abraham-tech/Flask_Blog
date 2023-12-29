# Flask Blog Application

This is a Flask blog application which includes features such as user registration, login, updating profiles with profile pictures, creating, updating and deleting blog posts.

## Features

- User Registration
- User Login & Logout
- User Profile Update
- Create, Update, Delete Posts
- Password Reset via Email

## Installation

- First, clone the repository using Git: 
- Create a Python virtual environment for the project:

    ```bash
    cd your-new-directory
    python3 -m venv env
    ```
  
- Activate the environment: 

    For macOS and Linux:

    ```bash
    source env/bin/activate
    ```
- Install the required packages using pip:

    ```bash
    pip install -r requirments.txt
    ```

## Running the Application

- You can run the application with the following command: 

    ```bash
    python app.py
    ```
  
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