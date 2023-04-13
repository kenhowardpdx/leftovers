from config import app
from models import *

@app.route("/")
def hello_world():
    data = {
        "message": "hello, world",
    }
    return data

@app.route("/users")
def users():
    return User.query.all()
