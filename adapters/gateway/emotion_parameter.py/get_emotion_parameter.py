from drivers.firebase.main import db


def get_emotion_parameter(user_id):
    try:
        get_emotion_parameter = db.child(user_id).child(
            "get_emotion_parameter").get()
    except Exception as error:
        print("error get bad evaluation texts:", error)
    else:
        print("success get bad evaluation texts")
        return get_emotion_parameter
