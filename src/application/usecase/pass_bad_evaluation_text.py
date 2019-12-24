from src.adapters.gateway.bad_evaluation_texts.read_bad_evaluation_texts import read_bad_evaluation_texts


def pass_bad_evaluation_texts(user_id):
    bad_evaluation_texts = read_bad_evaluation_texts(user_id)
    return bad_evaluation_texts
