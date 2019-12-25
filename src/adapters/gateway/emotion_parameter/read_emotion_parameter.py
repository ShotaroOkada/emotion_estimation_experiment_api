from src.drivers.firebase.app import db


def read_emotion_parameter(user_id):
    try:
        response = db.child("users").child(user_id).child(
            "emotion_parameter").get()
    except Exception as error:
        print("error read emotion parameter:", error)
    else:
        emotion_parameter = response.val()
        print("success read emotion parameter")
        return emotion_parameter
