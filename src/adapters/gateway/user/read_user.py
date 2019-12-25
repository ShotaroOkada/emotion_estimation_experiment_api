from src.drivers.firebase.app import db


def read_user(user_id):
    try:
        response = db.child("users").child(user_id).get()
    except Exception as error:
        print("error read user:", error)
    else:
        user = response.val()
        print("success read user")
        return user
