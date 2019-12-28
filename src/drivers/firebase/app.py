import pyrebase
from src.drivers.firebase.config import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
