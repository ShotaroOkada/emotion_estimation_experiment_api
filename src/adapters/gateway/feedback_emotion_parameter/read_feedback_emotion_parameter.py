from src.drivers.firebase.app import db
import json
import pprint


def read_feedback_emotion_parameter(user_id):
    try:
        response = db.child("users").child(user_id).child(
            "feedback_emotion_parameter").get()
    except Exception as error:
        print("error read feedback emotion parameter:", error)
    else:
        feedback_emotion_parameter = response.val()
        print("success read feedback emotion parameter")
        if feedback_emotion_parameter == None:
            print('feedback emotion parameter is null')
            return {}
        else:
            json_feedback_emotion_parameter = json.loads(
                feedback_emotion_parameter)
            pprint.pprint(json_feedback_emotion_parameter)
            return json_feedback_emotion_parameter
