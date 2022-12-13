from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author

# -------------------------------------
# ADDING book PAGE

@app.route('/all_books') #adding book page
def all_books():
    return render_template('all_books.html',all_books = Book.get_all())
    # adding books, we need to pass in the different books to allow the selection from the list, like above in /books

@app.route('/create_book',methods=['POST']) #creating book process and redirecting to book's author
def create_book():
    data = {
        "title":request.form['title'],
        "num_of_pages": request.form['num_of_pages'],
    }
    book_id = Book.save(data)
    return redirect('/all_books')

@app.route('/book/<int:id>')
def show_book(id):
    data = {
        "id" : id
    }
    return render_template('book.html',book=Book.get_by_id(data),unfavorited_authors=Author.unfavorited_authors(data))

@app.route('/add_author_favorite',methods=['POST'])
def add_author_favorite():
    data = {
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")