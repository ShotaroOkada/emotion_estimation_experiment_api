from adapters.gateway.emotion_parameter.get_emotion_parameter import get_emotion_parameter
from adapters.gateway.bad_evaluation_texts.get_bad_evaluation_texts import get_bad_evaluation_texts
from domain.service.translate_english import translate_english
from domain.service.nlu_estimation_emotion import nlu_estimation_emotion
from domain.service.morphological_analysis import morphological_analysis
from domain.service.apply_emotion_parameter import apply_emotion_parameter
from domain.service.convert_display_emotion_text import convert_display_emotion_text


def estimation_emotion(user_id, text):
    emotion_parameter = get_emotion_parameter(user_id)
    feature_words = morphological_analysis(text)
    english_text = translate_english(text)
    nlu_emotion_score = nlu_estimation_emotion(english_text)
    emotion_score_applied_parameter = apply_emotion_parameter(
        nlu_emotion_score, feature_words, emotion_parameter)
    display_emotion_text = convert_display_emotion_text(
        emotion_score_applied_parameter)

    return display_emotion_text
