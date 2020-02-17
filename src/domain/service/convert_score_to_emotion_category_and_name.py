#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.domain.entities.emotion import EmotionStrength
from src.domain.service.sort_nlu_score import sort_nlu_score
import pprint


def convert_score_to_emotion_category_and_name(emotion_score, emotions):
    sorted_emotion_score = sort_nlu_score(emotion_score)  # 型はタプル配列
    max_emotion_category, max_emotion_category_score = sorted_emotion_score[0]

    print('selected emotion category is', max_emotion_category)
    if max_emotion_category_score < 0.34:
        display_emotion_name = emotions[max_emotion_category][EmotionStrength.LOW.value]
    elif max_emotion_category_score < 0.67:
        display_emotion_name = emotions[max_emotion_category][EmotionStrength.MID.value]
    else:
        display_emotion_name = emotions[max_emotion_category][EmotionStrength.HIGH.value]

    print('display emotion name is', display_emotion_name)
    return {'name': display_emotion_name, 'category': max_emotion_category}
