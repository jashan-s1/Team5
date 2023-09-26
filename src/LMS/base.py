from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("start.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/user")
def user():
    return render_template("user.html")

