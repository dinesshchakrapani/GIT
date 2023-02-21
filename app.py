from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"
@app.route('/hello')
def welcome():
    name=request.args.get('x')
    return f"Welcome to {name} World"

app.run(host='0.0.0.0')