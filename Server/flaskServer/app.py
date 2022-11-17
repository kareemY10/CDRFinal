
from flask import Flask,render_template ,session ,redirect
from flask_mongoengine import MongoEngine
from flask_login import LoginManager, UserMixin
import pymongo
from functools import wraps
import sys
from user.Database import database
app = Flask(__name__)
DB=database.DataBase()
app.secret_key='temporary_secret'

def login_required(func):
    @wraps(func)
    def wrap(*arg,**Kwargs):
        if 'logged_in' in session:
            print(session)
            return func(*arg,**Kwargs)
        else :
            return redirect('/') #later should be redirected a 405 error 
    return wrap


from user import routes


arr={"Kareem": "Hi can you send me the the budget charts ...", "Microsoft": 'buy xbox today ...' , 'chris':'Hi I need you to push youre code asap ...','Mohammed':'Just sent you the database diagram ...'}

@app.route('/Home/')
@login_required
def Home():
    
	return render_template('Home.html',UserEmails=arr ,Loggedin=1 )




@app.route('/instructions')
def instruct():
    return render_template('ins.html')


@app.route('/')
def register():
    return render_template('signup.html')




if __name__ == '__main__':

	app.run()
