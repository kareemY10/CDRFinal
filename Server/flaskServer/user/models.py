from flask import Flask , jsonify , request
import uuid
from passlib.hash import pbkdf2_sha256
from user.Database import database

DB=database.DataBase()

class User:
    
    def signup():
        user={
            "_id":uuid.uuid4().hex,
            "email":request.form.get('email'),
            "password":request.form.get('passphrase')
        }
        DB.insert_user(request.form.get('email'))
        


        return jsonify(user) ,200
    

