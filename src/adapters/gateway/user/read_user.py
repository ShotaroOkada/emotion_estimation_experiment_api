from src.drivers.firebase.app import db


def read_user(user_id):
    try:
        user = db.child(user_id).get()
    except Exception as error:
        print("error read user:", error)
    else:
        print("success read user")
        return user
