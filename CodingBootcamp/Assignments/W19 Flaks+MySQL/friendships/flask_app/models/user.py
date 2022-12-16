from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friendship

class User:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # self.friends = [] How do I use this?

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        all_users_from_db =  connectToMySQL('friendships').query_db(query)
        all_users =[]
        for b in all_users_from_db:
            all_users.append(cls(b))
            print(b)
        return all_users

    @classmethod
    def get_users(cls):
        query = "SELECT * FROM friendships LEFT JOIN users ON users.id = user_id;"
        users_from_db =  connectToMySQL('friendships').query_db(query)
        users =[]
        for b in users_from_db:
            users.append(cls(b))
        return users
        
    @classmethod
    def get_friends(cls):
        query = "SELECT * FROM friendships LEFT JOIN users ON users.id = friend_id;"
        friends_from_db =  connectToMySQL('friendships').query_db(query)
        friends =[]
        for b in friends_from_db:
            friends.append(cls(b))
        return friends
    
    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users LEFT JOIN users.id = user_id WHERE user_id = %(id)s;"
        user_from_db = connectToMySQL('friendships').query_db(query,data)
        return cls(user_from_db[0])
    
    @classmethod
    def get_one_friend(cls,data):
        query = "SELECT * FROM users LEFT JOIN users.id = user_id WHERE friend_id = %(id)s;"
        user_from_db = connectToMySQL('friendships').query_db(query,data)
        return cls(user_from_db[0])
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name) VALUES (%(first_name)s,%(last_name)s);"
        return connectToMySQL('friendships').query_db(query,data)
    
    # @classmethod
    # def add_friendship(cls,data):
    #     query = "INSERT INTO friendships (user_id,friend_id) VALUES (%(user_id)s,%(friend_id)s);"
    #     return connectToMySQL('friendships').query_db(query,data)
    
    @classmethod
    def add_friendship(cls,data):
        if data["user_id"] != data["friend_id"]:
            query = "INSERT INTO friendships (user_id,friend_id) SELECT * FROM (SELECT %(user_id)s as user_id, %(friend_id)s as friend_id) as temp WHERE NOT EXISTS (SELECT user_id FROM friendships WHERE user_id = %(user_id)s and friend_id = %(friend_id)s or user_id = %(friend_id)s and friend_id = %(user_id)s) LIMIT 1;"
            return connectToMySQL('friendships').query_db(query,data)

        # why is this not working?
        # query = "INSERT INTO friendships (user_id,friend_id) VALUES (%(user_id)s,%(friend_id)s) WHERE NOT EXISTS (SELECT * FROM friendships WHERE user_id = %(user_id)s AND friend_id = %(friend_id)s);"