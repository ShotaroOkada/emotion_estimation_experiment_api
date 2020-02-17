#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import pprint
from src.domain.entities.emotion_parameter import initial_word_parameter
from src.domain.service.sort_nlu_score import sort_nlu_score


def update_emotion_parameter_to_user_evaluation(nlu_score, emotion_parameter, user_evaluation, entity_emotions, feature_words):
    is_new_feature_word = True
    estimated_emotion_category = user_evaluation["emotion_category"]
    evaluation_id = user_evaluation["evaluation_id"]
    sorted_nlu_score = sort_nlu_score(nlu_score)  # 型はタプル配列
    _, first_score = sorted_nlu_score[0]
    number_of_feature_words = len(feature_words)

    for feature_word in feature_words:
        if len(emotion_parameter):
            for word in emotion_parameter:
                if feature_word == word:
                    print('discovery same word: ', word)
                    if evaluation_id == "inappropriate":
                        _, second_score = sorted_nlu_score[0]
                        change_score = (
                            first_score - second_score + 0.000001) / number_of_feature_words
                        emotion_parameter[word][estimated_emotion_category] -= change_score
                    elif evaluation_id == "stronger":
                        if first_score < 0.34:
                            change_score = (0.34 - first_score) / \
                                number_of_feature_words
                            emotion_parameter[word][estimated_emotion_category] += change_score
                        elif first_score < 0.67:
                            change_score = (0.67 - first_score) / \
                                number_of_feature_words
                            emotion_parameter[word][estimated_emotion_category] += change_score
                        else:
                            print(
                                "parameter is not change because stonger and 0.67 over")
                    elif evaluation_id == "weaker":
                        if first_score < 0.34:
                            print(
                                "parameter is not change because weaker and 0.34 less")
                        elif first_score < 0.67:
                            change_score = (
                                first_score - 0.34 - 0.000001) / number_of_feature_words
                            for emotion_caterogy in entity_emotions:
                                emotion_parameter[word][emotion_caterogy] -= change_score
                        else:
                            change_score = (
                                first_score - 0.67 - 0.000001) / number_of_feature_words
                            for emotion_caterogy in entity_emotions:
                                emotion_parameter[word][emotion_caterogy] -= change_score
                    is_new_feature_word = False
        if(is_new_feature_word):
            print(feature_word, 'is new feature word')
            if(evaluation_id == "inappropriate" or "stronger" or "weaker"):
                new_word_parameter = copy.deepcopy(initial_word_parameter)
                new_word_parameter["word"] = feature_word
                if evaluation_id == "inappropriate":
                    _, second_score = sorted_nlu_score[0]
                    change_score = (first_score - second_score +
                                    0.000001) / number_of_feature_words
                    new_word_parameter[estimated_emotion_category] -= change_score
                elif evaluation_id == "stronger":
                    if first_score < 0.34:
                        change_score = (0.34 - first_score) / \
                            number_of_feature_words
                        new_word_parameter[emotion_caterogy] += change_score
                    elif first_score < 0.67:
                        change_score = (0.67 - first_score) / \
                            number_of_feature_words
                        new_word_parameter[emotion_caterogy] += change_score
                    else:
                        print(
                            "new word parameter is not change because stonger and 0.67 over")
                elif evaluation_id == "weaker":
                    if first_score < 0.34:
                        print("parameter is not change because weaker and 0.34 less")
                    elif first_score < 0.67:
                        change_score = (first_score - 0.34 -
                                        0.000001) / number_of_feature_words
                        for emotion_caterogy in entity_emotions:
                            new_word_parameter[emotion_caterogy] -= change_score
                    else:
                        change_score = (first_score - 0.67 -
                                        0.000001) / number_of_feature_words
                        for emotion_caterogy in entity_emotions:
                            new_word_parameter[emotion_caterogy] -= change_score
                emotion_parameter[feature_word] = new_word_parameter
        is_new_feature_word = True

    return emotion_parameter
