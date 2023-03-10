from routes import app
from werkzeug.serving import run_simple

if __name__ == "__main__":
    run_simple('localhost', 5001, app, use_reloader=True, use_debugger=True, use_evalex=True)