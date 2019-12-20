from src.drivers.firebase.main import db


def set_user(user_id):
    try:
        db.set(user_id)
    except Exception as error:
        print("error set user:", error)
    else:
        print("success set user")
