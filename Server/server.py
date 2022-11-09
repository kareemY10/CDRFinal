
from flask import Flask,render_template
from flask_mongoengine import MongoEngine
from flask_login import LoginManager, UserMixin
from dotenv import load_dotenv
import bson

from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:

        db = g._database = PyMongo(current_app).db
       
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)
app = Flask(__name__)

Loginmanger=LoginManager()
Loginmanger.init_app(app)












arr={"Kareem": "Hi can you send me the the budget charts ...", "Microsoft": 'buy xbox today ...' , 'chris':'Hi I need you to push youre code asap ...','Mohammed':'Just sent you the database diagram ...'}










@app.route('/Home')
def Home():
	return render_template('Home.html',UserEmails=arr ,Loggedin=1 )




@app.route('/')
def Login():
	return render_template('login.html')





if __name__ == '__main__':
	load_dotenv()

	app.run()
