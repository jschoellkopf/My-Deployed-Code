from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.title = db_data['title']
        self.num_of_pages = db_data['num_of_pages']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the authors that are associated with a book.
        self.authors_who_favorited = []

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL('books_schema').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        books_from_db =  connectToMySQL('books_schema').query_db(query)
        books =[]
        for b in books_from_db:
            books.append(cls(b))
        return books


    @classmethod 
    def get_by_id( cls , data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query , data )
        book = cls( results[0] )
        for row in results:
            # Now we parse the author data to make instances of authors and add them into our list.
            if row['authors.id'] == None:
                break
            data = {
                "id" : row["authors.id"],
                "name" : row["name"],
                "created_at" : row["authors.created_at"],
                "updated_at" : row["authors.updated_at"]
            }
            book.authors_who_favorited.append(author.Author(data))
        return book

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN (SELECT book_id FROM favorites WHERE author_id = %(id)s);"
        books = []
        results = connectToMySQL('books_schema').query_db(query,data)
        for row in results:
            books.append(cls(row))
        return books

    # not needed because does the exact same thing as in the author class
    # @classmethod
    # def add_favorite(cls,data):
    #     query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
    #     return connectToMySQL('books_schema').query_db(query,data)
