from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = current_app
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

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