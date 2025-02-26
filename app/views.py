from app import app
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/profile')
def profile():
    """Render the profile page."""
    user = {
        'image_url': 'Me.png',  # Put image in the static folder
        'full_name': 'Sheri-lee Mills',
        'username': '@smiles',
        'location': 'Portmore, Jamaica',
        'date_joined': datetime(2025, 2, 26),  
        'bio': 'I am who I am when I am and I am determined to do when I need to when I need to..',
        'posts': 7,
        'following': 250,
        'followers': 1000
    }
    formatted_date = format_date_joined(user['date_joined'])
    return render_template('profile.html', user=user, formatted_date=formatted_date)

def format_date_joined(date):
    """Format the date as Month, Year."""
    return date.strftime("%B, %Y")

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)



@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


