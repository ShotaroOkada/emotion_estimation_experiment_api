from src.adapters.gateway.emotion_parameter.read_emotion_parameter import read_emotion_parameter
from src.adapters.gateway.emotion_parameter.update_emotion_parameter import update_emotion_parameter
from src.adapters.gateway.feedback_emotion_parameter.read_feedback_emotion_parameter import read_feedback_emotion_parameter
from src.adapters.gateway.feedback_emotion_parameter.update_feedback_emotion_parameter import update_feedback_emotion_parameter
from src.adapters.gateway.evaluations.read_evaluations import read_evaluations
from src.adapters.gateway.emotions.read_emotions import read_emotions
from src.domain.service.morphological_analysis import morphological_analysis
from src.domain.service.update_emotion_parameter_to_user_evaluation import update_emotion_parameter_to_user_evaluation
import json


def apply_user_evaluation(user_id, user_evaluations):
    entity_evaluations = read_evaluations()
    entity_emotions = read_emotions()
    feature_words = morphological_analysis(
        user_evaluations['text'])
    feedback_emotion_parameter = read_feedback_emotion_parameter(user_id)
    new_feedback_emotion_parameter = update_emotion_parameter_to_user_evaluation(
        feedback_emotion_parameter, user_evaluations['algorithms']['feedback_algo'], entity_evaluations, entity_emotions, feature_words)
    update_feedback_emotion_parameter(user_id, new_feedback_emotion_parameter)

    if user_evaluations['previous_flag'] == True:
        return

    emotion_parameter = read_emotion_parameter(user_id)
    new_emotion_parameter = update_emotion_parameter_to_user_evaluation(
        emotion_parameter, user_evaluations['algorithms']['emotion_parameter_algo'], entity_evaluations, entity_emotions, feature_words)

    update_emotion_parameter(user_id, new_emotion_parameter)
