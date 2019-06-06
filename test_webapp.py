# FLASK_APP=test_webapp.py flask run
from flask import Flask as any_name
from student import Student

#app = Flask(__name__)
app = any_name(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/static")
def static_content():
    return app.send_static_file("static.html")

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
