from src.adapters.gateway.emotion_parameter.read_emotion_parameter import read_emotion_parameter
from src.domain.service.translate_english import translate_english
from src.domain.service.nlu_estimation_emotion import nlu_estimation_emotion
from src.domain.service.morphological_analysis import morphological_analysis
from src.domain.service.apply_emotion_parameter import apply_emotion_parameter
from src.domain.service.convert_display_emotion_text import convert_display_emotion_text
from src.adapters.gateway.emotions.read_emotions import read_emotions


def estimate_emotion(user_id, text):
    emotion_parameter = read_emotion_parameter(user_id)
    feature_words = morphological_analysis(text)
    english_text = translate_english(text)
    nlu_emotion_score = nlu_estimation_emotion(english_text)
    emotion_score_applied_parameter = apply_emotion_parameter(
        nlu_emotion_score, feature_words, emotion_parameter)
    emotions = read_emotions
    estimated_emotion_name = convert_display_emotion_text(
        emotion_score_applied_parameter, emotions)

    return estimated_emotion_name
