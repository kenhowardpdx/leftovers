from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    data = {
        "message": "hello, world",
    }
    return json.dumps(data)