from src.drivers.firebase.main import db


def read_emotion_parameter(user_id):
    try:
        emotion_parameter = db.child(user_id).child(
            "get_emotion_parameter").get()
    except Exception as error:
        print("error read emotion parameter:", error)
    else:
        print("success read emotion parameter")
        return emotion_parameter
