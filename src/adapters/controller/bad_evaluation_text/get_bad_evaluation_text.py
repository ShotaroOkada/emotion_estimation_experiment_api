from src.application.usecase.pass_bad_evaluation_text import pass_bad_evaluation_texts
from flask import Response
import json


def get_bad_evaluation_text(user_id):
    try:
        bad_evaluation_text = pass_bad_evaluation_texts(user_id)
    except Exception as error:
        print("error get bad evaluation text: ", error)
        return Response(status=400)
    else:
        print("success get bad evaluation text")
        return Response(response=json.dumps(bad_evaluation_text), status=200)
