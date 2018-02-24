from flask import render_template, flash, redirect
from app import app
from app.models import User
from flask import render_template
from app import app

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html', title='Travel Faster, Travel Better')
