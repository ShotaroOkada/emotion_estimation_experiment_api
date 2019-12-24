from src.application.usecase.apply_user_evaluation import apply_user_evaluation
from flask import Response


def post_evaluation(user_id, evaluation):
    try:
        apply_user_evaluation(user_id, evaluation)
    except Exception as error:
        print("error post evaluation: ", error)
        return(Response(status=200))
    else:
        print("success post evaluation")
        return(Response(status=200))
