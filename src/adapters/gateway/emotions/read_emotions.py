from src.drivers.firebase.app import db


def read_emotions():
    try:
        emotions = db.child("emotions").get()
    except Exception as error:
        print("error read emotions:", error)
    else:
        print("success read emotions")
        return emotions
