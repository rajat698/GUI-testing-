from flask import Flask, render_template, url_for

app = Flask(__name__)

PORT = 3200
HOST = '0.0.0.0'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)