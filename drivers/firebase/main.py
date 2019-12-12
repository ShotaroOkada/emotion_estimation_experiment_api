import pyrebase
from config import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
