#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

anger = ['苛立ち', '怒り', '激怒']
joy = ['ワクワク', '嬉しい', '幸せ']
sadness = ['切ない', '悲しい', '悲嘆']
fear = ['不安', '恐怖', '絶望']
disgust = ['うんざり', '嫌悪', '憎い']


class EmotionStrength(Enum):
    LOW = 0
    MID = 1
    HIGH = 2


class EmotionCategory(Enum):
    ANGER = 'anger'
    JOY = 'joy'
    SADNESS = 'sadness'
    FEAR = 'fear'
    DISGUST = 'disgust'


# emotions = [
#     {
#         'category_name': EmotionCategory.ANGER,
#         'category_emotions':  anger
#     },
#     {
#         'category_name': EmotionCategory.JOY,
#         'category_emotions':  joy
#     },
#     {
#         'category_name': EmotionCategory.SADNESS,
#         'category_emotions':  sadness
#     },
#     {
#         'category_name': EmotionCategory.FEAR,
#         'category_emotions':  fear
#     },
#     {
#         'category_name': EmotionCategory.DISGUST,
#         'category_emotions':  disgust
#     },
# ]

emotions = {
    EmotionCategory.ANGER: anger,
    EmotionCategory.DISGUST: disgust,
    EmotionCategory.FEAR: fear,
    EmotionCategory.JOY: joy,
    EmotionCategory.SADNESS: sadness
}

order_emotion_category = [EmotionCategory.ANGER, EmotionCategory.JOY,
                          EmotionCategory.SADNESS, EmotionCategory.FEAR, EmotionCategory.DISGUST]
