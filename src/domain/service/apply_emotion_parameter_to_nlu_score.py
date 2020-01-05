from src.domain.entities.emotion import EmotionCategory, order_emotion_category
import pprint


def apply_emotion_parameter_to_nlu_score(nlu_emotion_score, feature_words, emotion_parameter):
    for word in feature_words:
        for word_key in emotion_parameter:
            if word == word_key:
                for emotion_category in order_emotion_category:
                    nlu_emotion_score[emotion_category] += emotion_parameter[word_key][emotion_category]

    print('applied emotion parameter to nlu score is')
    pprint.pprint(nlu_emotion_score)
    return nlu_emotion_score
