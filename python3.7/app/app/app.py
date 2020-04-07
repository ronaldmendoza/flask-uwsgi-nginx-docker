from flask import Flask
from flask import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hiya! This is a Flask App'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def goodbye_world():
    return 'Good Bye, World!'

@app.route('/hello/<yourname>')
def greeting(yourname):
    return 'Hello %s' % escape(yourname)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
