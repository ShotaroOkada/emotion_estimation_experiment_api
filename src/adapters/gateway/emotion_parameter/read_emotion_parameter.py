from src.drivers.firebase.app import db
import json
import pprint


def read_emotion_parameter(user_id):
    try:
        response = db.child("users").child(user_id).child(
            "emotion_parameter").get()
    except Exception as error:
        print("error read emotion parameter:", error)
    else:
        emotion_parameter = response.val()
        print("success read emotion parameter")
        if emotion_parameter == None:
            print('emotion parameter is null')
            return {}
        else:
            json_emotion_parameter = json.loads(emotion_parameter)
            pprint.pprint(json_emotion_parameter)
            return json_emotion_parameter
