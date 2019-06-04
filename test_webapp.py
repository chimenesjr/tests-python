# FLASK_APP=test_webapp.py flask run
from flask import Flask as any_name
from student import Student

#app = Flask(__name__)
app = any_name(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
