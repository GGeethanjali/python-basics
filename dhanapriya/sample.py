from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, String, create_engine
app = Flask(__name__)
DATABASE_URL = "postgres+psycopg2://postgres:priya@localhost/Bookworld"
db = create_engine(DATABASE_URL)

@app.route("/")
def home():
    return "Welcome to !! <h1>Priya Book Store</h1>"

@app.route('/books',methods=['GET'])
def get_books():
    books = db.execute('select * from book.tblbookdetails')
    result = [dict(row) for row in books]
    return jsonify(result)

@app.route('/newbook', methods=['POST'])
def new_book():
    if request.method == 'POST':
        bookName = request.form['bookName']
        bookPrice = request.form['bookPrice']
        db.execute("INSERT INTO book.tblbookdetails(bookName,bookPrice) VALUES('{}','{}')".format(bookName,bookPrice))
        return 'New book inserted'

@app.route("/books/<name>/<price>")
def book(name,price):
    return f"book Name:{name},book price is:{price}"

if __name__ == '__main__' :
    app.run(debug=True)
