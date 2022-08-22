from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/time")
def current_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return "<h1>Current Time  : " +current_time +"<h1/>"

