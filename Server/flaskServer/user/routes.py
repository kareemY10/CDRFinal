from flask import Flask,render_template
from server import app
from user.models import User
from user.Database import database



@app.route('/users/signup' , methods=['POST'])
def sign():
    user=User.signup()
    DB=database.DataBase()
    DB.insert_user(user['email'])
    return 'k'