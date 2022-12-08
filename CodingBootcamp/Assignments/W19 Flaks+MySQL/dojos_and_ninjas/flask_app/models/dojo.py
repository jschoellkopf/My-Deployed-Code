from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the ninjas that are associated with a dojo.
        self.ninjas = []

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s, NOW(),NOW());"
        return connectToMySQL('Practice').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db =  connectToMySQL('Practice').query_db(query)
        dojos =[]
        for b in dojos_from_db:
            dojos.append(cls(b))
        return dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        dojo_from_db = connectToMySQL('Practice').query_db(query,data)
        return cls(dojo_from_db[0])

    # WHY DON'T I NEED THIS!!!???

    # @classmethod 
    # def get_dojo_with_ninjas( cls , data ):
    #     query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
    #     results = connectToMySQL('Practice').query_db( query , data )
    #     dojo = cls( results[0] )
    #     for row_from_db in results:
    #         # Now we parse the ninja data to make instances of ninjas and add them into our list.
    #         ninja_data = {
    #             "id" : row_from_db["ninjas.id"],
    #             "first_name" : row_from_db["ninjas.frsit_name"],
    #             "last_name" : row_from_db["last_name"],
    #             "age" : row_from_db["age"],
    #             #do we need a dojo_id value here?
    #             "created_at" : row_from_db["ninjas.created_at"],
    #             "updated_at" : row_from_db["ninjas.updated_at"]
    #         }
    #         dojo.ninjas.append(dojo.Ninja(ninja_data))
    #     return dojo
