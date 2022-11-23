
from flask import Flask,render_template ,session ,redirect

from functools import wraps
from user.Database import database
from user.Email.models import *
from user.Email.utils.receiver import *
from user.Email.models import user as SessionUser
app = Flask(__name__)
DB=database.DataBase()
app.secret_key='temporary_secret'

def login_required(func):
    @wraps(func)
    def wrap(*arg,**Kwargs):
        if 'logged_in' in session:
            return func(*arg,**Kwargs)
        else :
            return redirect('/') #later should be redirected a 405 error 
    return wrap


from user import routes


arr={"Kareem": "Hi can you send me the the budget charts ...", "Microsoft": 'buy xbox today ...' , 'chris':'Hi I need you to push youre code asap ...','Mohammed':'Just sent you the database diagram ...'}

@app.route('/Home/')
@login_required
def Home():



    CurrentUser=SessionUser.user(session.get('user')['email'],session.get('user')['password'],'imap.gmail.com')
    
    
    Reciver=EmailReceiver(CurrentUser,'Inbox')

    #ar1r=Reciver.receiver()
    #print(ar1r)

        

    return render_template('Home.html',UserEmails=arr ,Loggedin=1 )




@app.route('/instructions')
def instruct():
    return render_template('ins.html')


@app.route('/')
def register():
    return render_template('signup.html')




if __name__ == '__main__':

	app.run()
