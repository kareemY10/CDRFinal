
from flask import Flask,render_template
from flask_mongoengine import MongoEngine
from flask_login import LoginManager, UserMixin
import pymongo

import sys
from user.Database import database
app = Flask(__name__)



from user import routes




arr={"Kareem": "Hi can you send me the the budget charts ...", "Microsoft": 'buy xbox today ...' , 'chris':'Hi I need you to push youre code asap ...','Mohammed':'Just sent you the database diagram ...'}










@app.route('/Home')
def Home():
	return render_template('Home.html',UserEmails=arr ,Loggedin=1 )




@app.route('/')
def Login():
    return render_template('login.html')


@app.route('/Signup')
def register():
    return render_template('signup.html')




if __name__ == '__main__':

	app.run()
