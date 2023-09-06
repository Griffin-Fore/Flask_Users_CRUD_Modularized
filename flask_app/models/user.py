
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

class User:
    DB = 'users_cr'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    #Read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users
    
    # get one user
    @classmethod
    def show_one_user(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        data = {"user_id": user_id }
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    # Create/Insert
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, created_at, updated_at) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    # update one user
    @classmethod
    def update(cls, data):
        query = """UPDATE users
            SET first_name= %(first_name)s, last_name= %(last_name)s, email= %(email)s, updated_at= NOW()
            WHERE id= %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)

    # delete one user
    @classmethod
    def delete(cls, user_id):
        query = """ DELETE FROM users WHERE id = %(id)s;"""
        data = { "id" : user_id }
        return connectToMySQL(cls.DB).query_db(query, data)
    