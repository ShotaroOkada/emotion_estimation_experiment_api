from src.drivers.firebase.app import db


def read_feedback_emotion_parameter(user_id):
    try:
        response = db.child("users").child(user_id).child(
            "feedback_emotion_parameter").get()
    except Exception as error:
        print("error read feedback emotion parameter:", error)
    else:
        feedback_emotion_parameter = response.val()
        print("success read feedback emotion parameter")
        return feedback_emotion_parameter
