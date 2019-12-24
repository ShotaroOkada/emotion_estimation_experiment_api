from src.adapters.gateway.emotion_parameter.read_emotion_parameter import read_emotion_parameter
from src.adapters.gateway.feedback_emotion_parameter.read_feedback_emotion_parameter import read_feedback_emotion_parameter
from src.domain.service.morphological_analysis import morphological_analysis


def apply_user_evaluation(user_id, user_evaluations):
    emotion_parameter = read_emotion_parameter(user_id)
    feedback_emotion_parameter = read_feedback_emotion_parameter(user_id)
    feature_words = morphological_analysis(user_evaluations['nlu_algo'].text)
