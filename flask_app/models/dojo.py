
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import ninja

class Dojo:
    db = '20_dojos_and_ninjas_new'

    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # Create/Insert
    @classmethod
    def create_dojo(cls, data):
        query = """INSERT INTO dojos (name, created_at, updated_at) 
        VALUES (%(name)s, NOW(), NOW());"""
        return connectToMySQL(cls.db).query_db(query, data)
    
    # get one dojo with ninjas
    @classmethod
    def get_one_dojo_with_ninjas(cls, dojo_id):
        query = """SELECT *
        FROM dojos
        LEFT JOIN ninjas
        ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;"""

        data = {
            'id' : dojo_id
        }
        
        dojo_data = connectToMySQL(cls.db).query_db(query, data)
        this_dojo = cls(dojo_data[0])
        print("********************", dojo_data)
        
        for row in dojo_data:
            data = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'dojo_id' : row['dojo_id'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at']
            }
            this_dojo.ninjas.append(ninja.Ninja(data))
        return this_dojo

    #Read
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)

        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
