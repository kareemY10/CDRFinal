#Imports need to install : pyrebase
import pyrebase

config={
    "apiKey": "AIzaSyBei12InUCpoJEeQg52W6jLDm2YbH0Lt0k",
    "authDomain": "cdrfp-84c09.firebaseapp.com",
    "projectId": "cdrfp-84c09",
    "storageBucket": "cdrfp-84c09.appspot.com",
    "databaseURL":"https://cdrfp-84c09-default-rtdb.firebaseio.com/",
    "messagingSenderId": "1094946965755",
    "appId": "1:1094946965755:web:bbc5644de8479eea6c485e",
    "measurementId": "G-LFP3778DD2"
}

firebase=pyrebase.initialize_app(config=config)
database=firebase.database()
aa=database.child('Users').child('moh2003jb').get()
print(aa.val())