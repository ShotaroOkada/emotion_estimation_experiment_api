import copy
from src.domain.entities.emotion_parameter import initial_word_parameter


def update_emotion_parameter_to_user_evaluation(emotion_parameter, user_evaluation, entity_evaluations, entity_emotions, feature_words):
    new_word_parameter_flag = True
    estimated_emotion_category = user_evaluation["emotion_category"]
    evaluation_id = user_evaluation["evaluation_id"]
    change_score = entity_evaluations[evaluation_id].score

    for feature_word in feature_words:
        if len(emotion_parameter):
            for word_parameter in emotion_parameter:
                if feature_word == word_parameter["word"]:
                    if evaluation_id == "inappropriate" or "stronger":
                        word_parameter[estimated_emotion_category] += change_score
                    elif evaluation_id == "weaker":
                        for emotion_caterogy in entity_emotions:
                            word_parameter[emotion_caterogy] += change_score
                new_word_parameter_flag = False

        if(new_word_parameter_flag and (evaluation_id == "inappropriate" or "stronger" or "weaker")):
            new_word_parameter = copy.deepcopy(initial_word_parameter)
            new_word_parameter["word"] = feature_word
            if evaluation_id == "inappropriate" or "stronger":
                new_word_parameter[estimated_emotion_category] += change_score
            elif evaluation_id == "weaker":
                for emotion_caterogy in entity_emotions:
                    new_word_parameter[emotion_caterogy] += change_score
        emotion_parameter.append(new_word_parameter)
        new_word_parameter_flag = True

    return emotion_parameter
