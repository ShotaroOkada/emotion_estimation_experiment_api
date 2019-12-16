import pyrebase
from config import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
try:
    db.child("hoge").get()
except Exception as error:
    print("Error set", error)
else:
    print("Success")
