from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        'index.html')

@app.route("/route")
def route():
    return render_template(
        'route.html')

@app.route("/suggestions")
def suggestions():
    return render_template(
        'suggestions.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

# @app.route("/members/<string:name>/")
# def getMember(name):
#     return name
