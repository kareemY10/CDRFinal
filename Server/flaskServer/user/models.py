from flask import Flask , jsonify , request
import uuid
from passlib.hash import pbkdf2_sha256

class User:
    
    def signup():
        user={
            "_id":uuid.uuid4().hex,
            "email":request.form.get('email'),
            "password":request.form.get('passphrase')
        }
        
    
        return jsonify(user) ,200
    

