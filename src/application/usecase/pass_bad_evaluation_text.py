from src.adapters.gateway.bad_evaluation_texts.read_bad_evaluation_texts import read_bad_evaluation_texts
from src.adapters.gateway.bad_evaluation_texts.remove_bad_evaluation_texts import remove_bad_evaluation_text


def pass_bad_evaluation_texts(user_id):
    bad_evaluation_texts = read_bad_evaluation_texts(user_id)
    remove_bad_evaluation_text(user_id)
    return bad_evaluation_texts
