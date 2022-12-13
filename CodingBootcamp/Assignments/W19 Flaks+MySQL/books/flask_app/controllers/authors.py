from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author

# HOME PAGE
@app.route('/')
def home():
    return redirect('/authors')

@app.route('/authors') #base home page route
def all_authors():
    return render_template("all_authors.html",all_authors = Author.get_all())
    # for home page, we need the authors to showcase each one of them

@app.route('/create_author',methods=['POST']) #submits create author form from home page
def create_author():
    data = {
        "name":request.form['name'],
    }
    author_id = Author.save(data)
    return redirect('/authors')

@app.route('/author/<int:id>')
def author(id):
    data = {
        "id" : id
    }
    print(Book.get_by_id(data))
    # print(Author.unfavorited_authors(data))
    return render_template('author.html',author=Author.get_by_id(data),all_books=Book.unfavorited_books(data))

@app.route('/add_book_favorite',methods=['POST'])
def add_book_favorite():
    data = {
        'book_id' : request.form['book_id'],
        'author_id' : request.form['author_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")