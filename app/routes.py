from app import app
from flask import render_template

@app.route('/')
def index():
    context = {
        'users': ["Josh", "Nisarg", "Ken", "Tomas"]
    }
    return render_template('index.html', **context)


@app.route('/about')
def about():
    context = {
        'logged_in_user': "Nisarg",
        'info_to_display': "This is Flask...YEET"
    }
    return render_template('about.html', **context)