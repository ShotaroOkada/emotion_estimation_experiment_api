from drivers.firebase.main import db


def put_emotion_parameter(user_id, emotion_parameter):
    try:
        db.child(user_id).child(
            "get_emotion_parameter").put(emotion_parameter)
    except Exception as error:
        print("error put emotion parameter:", error)
    else:
        print("success put put emotion parameter")
