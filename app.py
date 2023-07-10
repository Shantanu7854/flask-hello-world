from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/jkl')
def hello_world_jkl():
    return 'Hello, World, jkl!'

@app.route('/api', methods=['POST'])
def buffet () :
    try:
        return '<h1>Data Added successfully!!!</h1>'
    except:
        return '<h1>invalid credentials!</h1>'

