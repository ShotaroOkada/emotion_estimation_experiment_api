from src.drivers.firebase.app import db


def read_bad_evaluation_texts(user_id):
    try:
        response = db.child("users").child(user_id).child(
            "bad_evaluation_texts").get()
    except Exception as error:
        print("error read bad evaluation texts:", error)
    else:
        bad_evaluation_texts = response.val()
        print("success read bad evaluation texts")
        return bad_evaluation_texts
