from src.drivers.firebase.main import db


def post_user(user_id):
    try:
        db.set(user_id)
    except Exception as error:
        print("error post user:", error)
    else:
        print("success post user")
