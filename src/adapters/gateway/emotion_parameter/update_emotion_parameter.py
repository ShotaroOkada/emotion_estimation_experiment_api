from src.drivers.firebase.app import db


def update_emotion_parameter(user_id, emotion_parameter):
    try:
        db.child("users").child(user_id).update(
            {"emotion_parameter": emotion_parameter})
    except Exception as error:
        print("error update emotion parameter:", error)
    else:
        print("success update put emotion parameter")
