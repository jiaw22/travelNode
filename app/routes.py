from flask import render_template, flash, redirect
from app import app
from flask import render_template
from flask import request, jsonify
# from generate import *

results = "";
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html', title='Travel Faster, Travel Better')

@app.route('/json', methods=["GET", "POST"])
def display():
     result = request.form
     return jsonify(request.form)

@app.route('/generate', methods=["GET", "POST"])
def route():
    # result = request.form
    # input0 = jsonify(request.form)
    # inputs = request.form.to_dict()
    # print inputs
    # google_input = calcLongLat(inputs)
    # times = generateTimeParam(inputs, google_input)
    # jia_output = calcUberWalking(google_input)
    # caroline_work = callCaroline(inputs, jia_output, times)
    #json.loads(j) string -> json for rids
    return render_template('route.html', title='Travel Faster, Travel Better pt. 2')
