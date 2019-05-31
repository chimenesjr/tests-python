# FLASK_APP=1flask.py flask run

from flask import Flask
app = Flask(__name__)

@app.route("/")
def flask():
    return "Hello World!"

@app.route("/user/<username>")
def show_user(username):
    return "User: %s" % username