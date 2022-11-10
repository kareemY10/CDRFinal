from flask import Flask
from server import app
from user.models import User



@app.route('/users/signup' , methods=['GET'])
def sign():
    return User().signup()