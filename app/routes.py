from flask import render_template, flash, redirect
from app import app
from flask import render_template
from flask import request, jsonify
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html', title='Travel Faster, Travel Better')

@app.route('/json', methods=["GET", "POST"])
def display():
     result = request.form
     return jsonify(request.form)

@app.route('/route', methods=["GET", "POST"])
def route():
     return render_template('route.html', title='Travel Faster, Travel Better pt. 2')
