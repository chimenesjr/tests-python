# FLASK_APP=1flask.py flask run

from flask import Flask, render_template
app = Flask(__name__)

# @app.route("/")
# def flask():
#     return "Hello World!"

@app.route("/static")
def static_content():
    return app.send_static_file("static.html")

@app.route("/profile/<name>")
def flask(name):
    return render_template("profile.html", name=name)

@app.route("/user/<username>")
def show_user(username):
    return "User: %s" % username