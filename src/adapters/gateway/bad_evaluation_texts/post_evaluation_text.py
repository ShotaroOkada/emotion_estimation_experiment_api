from src.drivers.firebase.main import db


def post_bad_evaluation_text(user_id, bad_evaluation_text):
    try:
        db.child(user_id).child(
            "bad_evaluation_texts").set(bad_evaluation_text)
    except Exception as error:
        print("error post bad evaluation texts:", error)
    else:
        print("success post bad evaluation texts")
