from flask import Flask, render_template, redirect,request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about(about):
    return "<h1 style = 'color: red'> About !!!!!!!!!!!!!! </h1> "



if __name__ == "__main__":
    app.run(debug = True )