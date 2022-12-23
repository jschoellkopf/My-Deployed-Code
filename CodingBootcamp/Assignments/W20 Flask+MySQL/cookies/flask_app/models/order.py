# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash, session

class Order:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.amount = data['amount']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('cookies').query_db(query)
        # Create an empty list to append our instances of friends
        orders = []
        # Iterate over the db results and create instances of friends with cls.
        for order in results:
            orders.append( cls(order) )
        return orders
    
    # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO orders (name , type , amount, created_at, updated_at) VALUES ( %(name)s , %(type)s , %(amount)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('cookies').query_db( query, data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM orders WHERE id = %(id)s"
        result = connectToMySQL('cookies').query_db(query, data)
        return cls(result[0])
        #result is a list

    @classmethod
    def update(cls,data):
        query = "UPDATE orders SET name=%(name)s,type=%(type)s,amount=%(amount)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('cookies').query_db(query,data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM orders WHERE id=%(id)s;"
        return connectToMySQL('cookies').query_db(query,data)
            
    @staticmethod
    def validate_order(order):
        is_valid = True # we assume this is true
        if len(order['name']) < 2:
            flash("Name must be at least 2 characters.", 'name')
            is_valid = False
        if len(order['type']) < 2:
            flash("Type must be at least 2 characters.", 'type')
            is_valid = False
        if float(order['amount']) < 0: 
            flash("Invalid amount!", 'amount')
            is_valid = False
        session['name'] = order['name']
        session['type'] = order['type']
        session['amount'] = order['amount']
        return is_valid