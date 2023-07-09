from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/jkl')
def hello_world_jkl():
    return 'Hello, World, jkl!'


