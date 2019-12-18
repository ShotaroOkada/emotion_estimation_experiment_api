from src.drivers.firebase.main import db


def delete_bad_evaluation_text(user_id):
    try:
        db.child(user_id).child(
            "bad_evaluation_texts").remove()
    except Exception as error:
        print("error delete bad evaluation texts:", error)
    else:
        print("success delete bad evaluation texts")
