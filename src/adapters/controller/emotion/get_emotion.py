from src.application.usecase.estimate_emotion import estimate_emotion
from flask import Response
import json


def get_emotion(user_id, text_info):
    try:
        estimated_emotion = estimate_emotion(user_id, text_info['text'])
    except Exception as error:
        print("error get emotion: ", error)
        return Response(status=400)
    else:
        print("success get emotion")
        return Response(response=json.dumps(estimated_emotion), status=200)
