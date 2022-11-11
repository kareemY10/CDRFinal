from flask import Flask,render_template
from server import app
from user.models import User



@app.route('/users/signup' , methods=['POST'])
def sign():
    user=User.signup()
    print(user[0])
    print('bom bom bom')
    return 'k'