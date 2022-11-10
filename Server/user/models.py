from flask import Flask , jsonify

class User():
    def signup(self):
        user={
            "_id":"",
            "email":"",
            "password":""
        }
    
        return jsonify(user) ,200
    

