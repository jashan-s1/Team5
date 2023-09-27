import database_connection as dbc

def issue_book(bookID, userID, issueDate):
    dbc.Issued.query.add(bookID, userID, issueDate)
    dbc.Issued.commit()

def return_book(bookID, userID, returnDate):
    dbc.History.query.add(bookID, userID, dbc.Issued.query.filter_by(bookID=bookID, userID=userID)[0]['issueDate'], returnDate)
    dbc.Issued.query.filter_by(bookID=bookID, userID=userID).delete()
    dbc.Issued.commit()
    dbc.History.commit()

def add_book(bookID, title, author, publisher, isbn, year):
    dbc.Book.query.add(bookID, title, author, publisher, isbn, year)
    dbc.Book.commit()

def new_book(srNo, bookID, status):
    dbc.Library.query.add(srNo, bookID, status)
    dbc.Library.commit()