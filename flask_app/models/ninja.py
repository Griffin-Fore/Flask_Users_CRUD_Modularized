
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

class Ninja:
    db = '20_dojos_and_ninjas_new'

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    # Create/Insert
    @classmethod
    def create_ninja(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo)s, NOW(), NOW());"""
        ninja_id = connectToMySQL(cls.db).query_db(query, data)
        return ninja_id