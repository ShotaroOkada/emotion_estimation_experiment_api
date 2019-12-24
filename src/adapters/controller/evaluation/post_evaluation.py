from src.application.usecase.apply_user_evaluation import apply_user_evaluation


def post_evaluation(user_id, evaluation):
    apply_user_evaluation(user_id, evaluation)
    return 0
