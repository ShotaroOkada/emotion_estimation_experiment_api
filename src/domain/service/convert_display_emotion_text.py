from src.domain.entities.emotions import emotions, EmotionStrength


def convert_display_emotion_text(emotion_score):
    max_emotion_category_score = -10

    for emotion_category in emotion_score:
        emotion_category_score = emotion_score[emotion_category]
        if max_emotion_category_score < emotion_category_score:
            max_emotion_category_score = emotion_category_score
            max_emotion_category = emotion_category

    if max_emotion_category_score < 0.34:
        display_emotion_text = emotions[max_emotion_category][EmotionStrength.LOW]
    elif max_emotion_category_score < 0.67:
        display_emotion_text = emotions[max_emotion_category][EmotionStrength.MID]
    else:
        display_emotion_text = emotions[max_emotion_category][EmotionStrength.HIGH]

    return display_emotion_text
