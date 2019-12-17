from domain.entities.emotions import EmotionCategory, order_emotion_category


def apply_emotion_parameter(nlu_emotion_score, feature_words, emotion_parameter):
    for word in feature_words:
        for word_parameter in emotion_parameter:
            if word == word_parameter['word']:
                for emotion_category in order_emotion_category:
                    nlu_emotion_score[emotion_category] += word_parameter[emotion_category]

    return nlu_emotion_score
