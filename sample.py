from flask import Flask,url_for,request

app = Flask(__name__)
@app.route('/')
def index():
    url = url_for('hello')
    return f'The URL for the hello() function is: {url}'

@app.route('/hello_world')
def hello():
    data=request.args.get('x')
    return f'Hello {data}!'
if __name__=="__main__":
    app.run(host="0.0.0.0")