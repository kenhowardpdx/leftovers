from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    data = {
        "message": "hello, world",
    }
    return data