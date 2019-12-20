from src.drivers.firebase.main import db


def read_bad_evaluation_texts(user_id):
    try:
        bad_evaluation_texts = db.child(user_id).child(
            "bad_evaluation_texts").get()
    except Exception as error:
        print("error read bad evaluation texts:", error)
    else:
        print("success read bad evaluation texts")
        return bad_evaluation_texts
