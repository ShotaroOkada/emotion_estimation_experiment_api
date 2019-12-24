from src.drivers.firebase.app import db


def set_user(user_id):
    try:
        db.child("users").child(user_id).set({
            "emotion_parameter": {},
            "feedback_emotion_parameter": {},
            "nlu_algo_evaluations": {
            },
            "emotion_parameter_algo_evaluations": {
            },
            "feedback_algo_evaluations": {
            },
            "bad_evaluation_texts": []
        })
    except Exception as error:
        print("error set user:", error)
    else:
        print("success set user")
