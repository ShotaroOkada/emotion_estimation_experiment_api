import copy
import pprint
from src.domain.entities.emotion_parameter import initial_word_parameter


def update_emotion_parameter_to_user_evaluation(emotion_parameter, user_evaluation, entity_evaluations, entity_emotions, feature_words):
    print('pass 0')
    new_word_parameter_flag = True
    estimated_emotion_category = user_evaluation["emotion_category"]
    evaluation_id = user_evaluation["evaluation_id"]
    change_score = entity_evaluations[evaluation_id]['score']

    print('pass 1')
    for feature_word in feature_words:
        print('pass 1.1')
        if len(emotion_parameter):
            print('pass 1.2')
            for word in emotion_parameter:
                pprint.pprint(word)
                if feature_word == word:
                    print('pass 1.3')
                    if evaluation_id == "inappropriate" or "stronger":
                        print('pass 1.4')
                        emotion_parameter[word][estimated_emotion_category] += change_score
                        print('pass 1.5')
                    elif evaluation_id == "weaker":
                        print('pass 1.6')
                        for emotion_caterogy in entity_emotions:
                            emotion_parameter[word][emotion_caterogy] += change_score
                            print('pass 1.7')
                    new_word_parameter_flag = False
        print('pass 2')
        if(new_word_parameter_flag):
            if(evaluation_id == "inappropriate" or "stronger" or "weaker"):
                new_word_parameter = copy.deepcopy(initial_word_parameter)
                print('change score is')
                print(change_score)
                print('new word parameter is')
                pprint.pprint(new_word_parameter)
                new_word_parameter["word"] = feature_word
                if evaluation_id == "inappropriate" or "stronger":
                    new_word_parameter[estimated_emotion_category] += change_score
                    print('new score is ',
                          new_word_parameter[estimated_emotion_category])
                elif evaluation_id == "weaker":
                    for emotion_caterogy in entity_emotions:
                        new_word_parameter[emotion_caterogy] += change_score
                        print('new score is ',
                              new_word_parameter[emotion_caterogy])
                emotion_parameter[feature_word] = new_word_parameter
        new_word_parameter_flag = True
        print('pass 3')

    print('pass 4')
    return emotion_parameter
