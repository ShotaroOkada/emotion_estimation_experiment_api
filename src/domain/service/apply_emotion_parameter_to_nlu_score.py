from src.domain.entities.emotion import EmotionCategory, order_emotion_category
import pprint


def apply_emotion_parameter_to_nlu_score(nlu_emotion_score, feature_words, emotion_parameter):
    for word in feature_words:
        for word_parameter in emotion_parameter:
            if word == word_parameter['word']:
                for emotion_category in order_emotion_category:
                    print(nlu_emotion_score)
                    print(nlu_emotion_score[emotion_category])
                    nlu_emotion_score[emotion_category] += word_parameter[emotion_category]

    print('applied emotion parameter to nlu score is')
    pprint.pprint(nlu_emotion_score)
    return nlu_emotion_score
