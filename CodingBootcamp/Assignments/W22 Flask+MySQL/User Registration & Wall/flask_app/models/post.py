# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash, session
from flask_bcrypt import Bcrypt
from flask_app.__init__ import app
from flask_app.models.user import User
bcrypt = Bcrypt(app)
import re

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.user = data['user']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO posts (content , user_id, created_at, updated_at) VALUES ( %(content)s , %(user_id)s , NOW(), NOW());"
        return connectToMySQL('registration_login').query_db( query, data)

    @classmethod
    def delete(cls, post_id):
        query = "DELETE from posts WHERE id = %(id)s;"
        return connectToMySQL('registration_login').query_db( query, { "id" : post_id} )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id ORDER BY posts.id DESC"
        results = connectToMySQL('registration_login').query_db(query)
        all_posts = []
        for row in results:
            posting_user = User({
                "id" : row["user_id"],
                "email" : row['email'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at'],
                "password" : row['password']
            })
            new_post = Post({
                "id" : row["id"],
                "content" : row['content'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at'],
                "user" : posting_user,
            })
            all_posts.append(new_post)
        return all_posts


    @staticmethod
    def validate_post(post):
        is_valid = True # we assume this is true
        if len(post['post_content']) < 1:
            flash("Cannot be empty", 'post_content')
            is_valid = False
        return is_valid