from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/admin")
def login_admin():
    return render_template("login_admin.html")

@app.route("/login/user")
def login_user():
    return render_template("login_user.html")

@app.route("/register/admin")
def register_admin():
    return render_template("register_admin.html")

@app.route("/register/user")
def register_user():
    return render_template("register_user.html")

@app.route("/admin/addbook")
def add_book():
    return render_template("add_book.html")

@app.route("/admin/returnbook")
def return_book():
    return render_template("return_book.html")


if __name__ == "__main__":
    app.run()