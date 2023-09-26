from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/registeradmin")
def registeradmin():
    return render_template("registeradmin.html")

@app.route("/registeruser")
def registeruser():
    return render_template("registeruser.html")

@app.route("/admin/addbook")
def addbook():
    return render_template("add_book.html")

@app.route("/admin/returnbook")
def returnbook():
    return render_template("return_book.html")
