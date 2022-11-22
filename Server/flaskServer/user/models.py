from flask import Flask , jsonify , request ,session,redirect
import uuid
from passlib.hash import pbkdf2_sha256
from user.Database import database

DB=database.DataBase()

class User:

    def start_session(self,user):
        session['logged_in']=True

        session['user']=user
        return jsonify(user),200

    
    def signup(self):
        user={
            "_id":uuid.uuid4().hex,
            "email":request.form.get('email'),
            "password":request.form.get('passphrase')
        }

        
        status=DB.insert_user(user['email'],user['password']) 
        print('i am status '+ str(status))
        #status=False
        if status==False:
            print('big big problem')
            return jsonify({"error":"Email address already in use"}) ,400
            

        if status==True:
            print('every thing is fine')
            return self.start_session(user)   
    def signout(self):
        session.clear()
        return redirect('/')

