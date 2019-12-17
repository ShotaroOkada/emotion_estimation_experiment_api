from drivers.firebase.main import db


def put_bad_evaluation_text(user_id, bad_evaluation_texts):
    try:
        db.child(user_id).child(
            "bad_evaluation_texts").update(bad_evaluation_texts)
    except Exception as error:
        print("error put bad evaluation texts:", error)
    else:
        print("success put bad evaluation texts")
