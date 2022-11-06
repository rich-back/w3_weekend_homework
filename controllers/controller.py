from flask import render_template
from app import app
from models.book_list import books
from models.book import Book




@app.route('/library')
def index():
    return render_template('index.html', title='Home', books=books)


@app.route('/library/<index>')
def single_book(index):
    selected_book = books[int(index)]
    return render_template('book.html', book=selected_book)