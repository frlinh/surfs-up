from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# Run 'set FLASK_APP=app.py' in terminal for Windows
# 'flask run' in terminal