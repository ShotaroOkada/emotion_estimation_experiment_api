from src.drivers.firebase.app import db


def push_bad_evaluation_text(user_id, bad_evaluation_text):
    try:
        db.child("users").child(user_id).child(
            "bad_evaluation_texts").push(bad_evaluation_text)
    except Exception as error:
        print("error push bad evaluation texts:", error)
    else:
        print("success push bad evaluation texts")
