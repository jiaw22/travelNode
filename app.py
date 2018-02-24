from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        'index.html',name=name)

@app.route("/route")
def hello():
    return "Hello World!"

@app.route("/suggestions")
def members():
    return "Members"

# @app.route("/members/<string:name>/")
# def getMember(name):
#     return name

if __name__ == "__main__":
    app.run(host='travelNode.tech', port=80)
