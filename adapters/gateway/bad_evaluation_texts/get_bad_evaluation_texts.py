from drivers.firebase.main import db


def get_bad_evaluation_texts(user_id):
    try:
        bad_evaluation_texts = db.child(user_id).child(
            "bad_evaluation_texts").get()
    except Exception as error:
        print("error get bad evaluation texts:", error)
    else:
        print("success get bad evaluation texts")
        return bad_evaluation_texts
