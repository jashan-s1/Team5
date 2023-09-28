from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.app_context()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False
db= SQLAlchemy(app)
migrate = Migrate(app, db)
 
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20))
    user_email = db.Column(db.String(20), nullable=False)
    user_password = db.Column(db.String(20), nullable=False)
    mobile_no = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.user_id} - {self.first_name}"

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    publisher = db.Column(db.String(20), nullable=False)
    book_isbn = db.Column(db.Integer, nullable=False)
    book_year = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.book_id} - {self.title}"

class Library(db.Model):
    serial_no = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.serial_no} - {self.book_id}"

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_no = db.Column(db.Integer, db.ForeignKey('library.serial_no'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id} - {self.serial_no}"

class Issued(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_no = db.Column(db.Integer, db.ForeignKey('library.serial_no'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id} - {self.serial_no}"

@app.route("/")
def index():
    data= User(user_id=7554, first_name="Jashandeep")
    db.session.add(data)
    db.session.commit()
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

@app.route("/admin/addbook", methods=["GET", "POST"])
def add_book():
    return render_template("add_book.html")

@app.route("/admin/returnbook")
def return_book():
    return render_template("return_book.html")


if __name__ == "__main__":
    app.run(debug=True)