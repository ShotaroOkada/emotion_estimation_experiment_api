from src.application.usecase.login import login
from flask import Response


def post_user(user_id):
    try:
        login(user_id)
    except Exception as error:
        print("error post user: ", error)
        return Response(status=400)
    else:
        print("success post user")
        return Response(status=200)
