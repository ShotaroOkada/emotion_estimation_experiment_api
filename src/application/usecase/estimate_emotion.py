from src.adapters.gateway.emotion_parameter.read_emotion_parameter import read_emotion_parameter
from src.domain.service.translate_english import translate_english
from src.domain.service.nlu_estimation_emotion import nlu_estimation_emotion
from src.domain.service.morphological_analysis import morphological_analysis
from src.domain.service.apply_emotion_parameter_to_nlu_score import apply_emotion_parameter_to_nlu_score
from src.domain.service.convert_score_to_emotion_category_and_name import convert_score_to_emotion_category_and_name
from src.adapters.gateway.emotions.read_emotions import read_emotions
from src.adapters.gateway.feedback_emotion_parameter.read_feedback_emotion_parameter import read_feedback_emotion_parameter


def estimate_emotion(user_id, text_info):
    emotions = read_emotions()
    feedback_emotion_parameter = read_feedback_emotion_parameter(user_id)
    feature_words = morphological_analysis(text_info['text'])
    english_text = translate_english(text_info['text'])
    nlu_emotion_score = nlu_estimation_emotion(english_text)
    emotion_score_applied_feedback_parameter = apply_emotion_parameter_to_nlu_score(
        nlu_emotion_score, feature_words, feedback_emotion_parameter
    )
    feedback_parameter_estimated_emotion = convert_score_to_emotion_category_and_name(
        emotion_score_applied_feedback_parameter, emotions
    )

    if text_info['previous_flag']:

        response_object = {
            "text": text_info['text'],
            "previous_flag": text_info['previous_flag'],
            "algorithms": {
                "feedback_algo": {
                    "algorithm_id": "feedback_algo",
                    "emotion_category": feedback_parameter_estimated_emotion['category'],
                    "emotion_name": feedback_parameter_estimated_emotion['name']
                }
            }
        }

        return response_object

    emotion_parameter = read_emotion_parameter(user_id)
    emotion_score_applied_parameter = apply_emotion_parameter_to_nlu_score(
        nlu_emotion_score, feature_words, emotion_parameter)
    nlu_estimated_emotion = convert_score_to_emotion_category_and_name(
        nlu_emotion_score, emotions)
    parameter_estimated_emotion = convert_score_to_emotion_category_and_name(
        emotion_score_applied_parameter, emotions
    )

    response_object = {
        "text": text_info['text'],
        "previous_flag": text_info['previous_flag'],
        "algorithms": {
            "nlu_algo": {
                "algorithm_id": "nlu_algo",
                "emotion_category": nlu_estimated_emotion['category'],
                "emotion_name": nlu_estimated_emotion['name']
            },
            "emotion_parameter_algo": {
                "algorithm_id": "emotion_parameter_algo",
                "emotion_category": parameter_estimated_emotion['category'],
                "emotion_name": parameter_estimated_emotion['name']
            },
            "feedback_algo": {
                "algorithm_id": "feedback_algo",
                "emotion_category": feedback_parameter_estimated_emotion['category'],
                "emotion_name": feedback_parameter_estimated_emotion['name']
            }
        }
    }

    return response_object
