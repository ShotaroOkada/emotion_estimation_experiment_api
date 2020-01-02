from src.application.usecase.apply_user_evaluation import apply_user_evaluation
from src.application.usecase.add_bad_evaluation_text_from_user_evaluations import add_bad_evaluation_text_from_user_evaluations
from src.application.usecase.record_user_evaluation_for_each_algorithm import record_user_evaluation_for_each_algorithm
from flask import Response


def post_evaluation(user_id, evaluation):
    try:
        apply_user_evaluation(user_id, evaluation)
    except Exception as error:
        print("error post evaluation: ", error)
        return(Response(status=400))
    else:
        print("success post evaluation")
        add_bad_evaluation_text_from_user_evaluations(user_id, evaluation)
        record_user_evaluation_for_each_algorithm(user_id, evaluation)
        return(Response(status=200))
