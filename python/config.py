from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from os import environ
from sqlalchemy import URL

db_uri = URL.create(
    "postgresql+psycopg2",
    username=environ.get("DB_USER"),
    password=environ.get("DB_PASSWORD"),
    host=environ.get("DB_HOST"),
    database=environ.get("DB_NAME"),
)

print(f"${db_uri=}")
 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.errorhandler(500)
def internal_error(error):
    return {"status": 500, "message": "Internal Server Error"}
