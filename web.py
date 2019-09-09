from flask import Flask
app = Flask (__name__)

@app.route('/')
def index():
    return 'this website using Flask as a framework'
