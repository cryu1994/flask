from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template("index.html")
@app.route('/success.html')
def sucess():
    return render_template("success.html")

@app.route('/about.html')
def about():
    return render_template("about.html")
app.run(debug=True)
