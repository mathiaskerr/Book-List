from flask import render_template, request, redirect    
from app import app
from models.book import Book
from models.book_list import book_list, add_new_book, delete_book

@app.route('/books')
def index():
    return render_template("index.html", title = "Home", book_list=book_list )

@app.route('/books', methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    add_new_book(new_book)
    return render_template("index.html", title = "Home", book_list=book_list)

@app.route('/books/<int:id>')
def single_book(id):
    return render_template(
        "book.html" , title="Book", book=book_list[id]
    )

@app.route('/books/delete/<id>', methods=["POST"])
def remove_book(id):    
    if "delete" in request.form:
        delete_book(id)
    return redirect('/books')
