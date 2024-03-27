from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message

app = Flask(__name__)



mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/todoList")
def todoList():
    return render_template("todoList.html")

@app.route("/blogPost")
def blogPost():
    return render_template("blogPost.html")

@app.route("/apiRest")
def apiRest():
    return render_template("apiRest.html")