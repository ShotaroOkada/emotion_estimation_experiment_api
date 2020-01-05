from src.domain.entities.emotion import EmotionStrength
import pprint


def convert_score_to_emotion_category_and_name(emotion_score, emotions):
    max_emotion_category_score = -10

    for emotion_category in emotion_score:
        emotion_category_score = emotion_score[emotion_category]
        if max_emotion_category_score < emotion_category_score:
            max_emotion_category_score = emotion_category_score
            max_emotion_category = emotion_category

    print('selected emotion category is', max_emotion_category)
    if max_emotion_category_score < 0.34:
        display_emotion_name = emotions[max_emotion_category][EmotionStrength.LOW.value]
    elif max_emotion_category_score < 0.67:
        display_emotion_name = emotions[max_emotion_category][EmotionStrength.MID.value]
    else:
        display_emotion_name = emotions[max_emotion_category][EmotionStrength.HIGH.value]

    print('display emotion name is', display_emotion_name)
    return {'name': display_emotion_name, 'category': max_emotion_category}
