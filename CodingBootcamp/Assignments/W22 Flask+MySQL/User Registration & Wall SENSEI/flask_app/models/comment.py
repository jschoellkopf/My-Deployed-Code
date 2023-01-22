# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash, session
from flask_bcrypt import Bcrypt
from flask_app.__init__ import app
from flask_app.models.user import User
bcrypt = Bcrypt(app)
import re

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.comment = data['comment']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO comments (comment , user_id, post_id, created_at, updated_at) VALUES ( %(comment)s , %(user_id)s , %(post_id)s, NOW(), NOW());"
        return connectToMySQL('registration_login').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM comments"
        results = connectToMySQL('registration_login').query_db(query)
        print(results[0])
        all_comments = []
        for row in results:
            one_comment = cls(row)
            # comment = Comment({
            #     "id" : row["id"],
            #     "comment" : row['comment'],
            #     "user_id" : row['user_id'],
            #     "post_id" : row['post_id'],
            #     "created_at" : row['created_at'],
            #     "updated_at" : row['updated_at'],
            # })
            all_comments.append(one_comment)
        return all_comments

    @staticmethod
    def validate_comment(comment):
        is_valid = True # we assume this is true
        if len(comment['comment']) < 1:
            flash("Cannot be empty", 'comment')
            is_valid = False
        return is_valid