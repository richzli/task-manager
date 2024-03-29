from flask import render_template

from taskmanager.app import app


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/app/")
def app():
    tasks = core.get_tasks()
    return render_template()