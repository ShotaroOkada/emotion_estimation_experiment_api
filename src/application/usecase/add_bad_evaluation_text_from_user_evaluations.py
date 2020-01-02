from src.adapters.gateway.bad_evaluation_texts.push_evaluation_text import push_bad_evaluation_text
import pprint
from src.domain.entities.evaluation import EvaluationName


def add_bad_evaluation_text_from_user_evaluations(user_id, user_evaluations):
    feedback_algo_evaluation = user_evaluations['feedback_algo']
    if feedback_algo_evaluation['previous_flag'] == True:
        print("Did not add text because previos flag is True")
    elif feedback_algo_evaluation['evaluation_id'] == EvaluationName.APPROPRIATE.value:
        print("Did not add text because evaluation is appropriate")
    elif feedback_algo_evaluation['evaluation_id'] == EvaluationName.UNKNOWN.value:
        print("Did not add text because evaluation is unknown")
    else:
        push_data = {
            "previous_flag": True,
            "text": feedback_algo_evaluation['text']
        }
        try:
            push_bad_evaluation_text(user_id, push_data)
        except Exception as error:
            print("error add false flag bad evaluation text: ", error)
        else:
            print("success add false flag bad evaluation text")
            pprint.pprint(push_data)
