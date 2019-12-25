from src.drivers.firebase.app import db


def read_emotions():
    try:
        response = db.child("emotions").get()
    except Exception as error:
        print("error read emotions:", error)
    else:
        emotions = response.val()
        print("success read emotions")
        return emotions
