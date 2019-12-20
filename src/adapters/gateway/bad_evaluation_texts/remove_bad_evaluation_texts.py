from src.drivers.firebase.main import db


def remove_bad_evaluation_text(user_id):
    try:
        db.child(user_id).child(
            "bad_evaluation_texts").remove()
    except Exception as error:
        print("error remove bad evaluation texts:", error)
    else:
        print("success remove bad evaluation texts")
