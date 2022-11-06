from flask import render_template, request, redirect
from app import app
from models.book_list import books
from models.book import Book
from models.book_list import add_new_book, remove_book




@app.route('/library')
def index():
    return render_template('index.html', title='Home', books=books)


@app.route('/library/<index>')
def single_book(index):
    selected_book = books[int(index)]
    return render_template('book.html', book=selected_book)

@app.route('/library', methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return render_template('index.html', title='Home', books=books)

@app.route('/library/delete/<title>', methods=['POST'])
def delete(title):
  remove_book(title)
  return redirect('/library')