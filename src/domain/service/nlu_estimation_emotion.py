#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.drivers.nlu.main import natural_language_understanding
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions


def nlu_estimation_emotion(text):
    # テキストから感情を返してもらう
    response = natural_language_understanding.analyze(
        features=Features(emotion=EmotionOptions(targets=None)),
        text=text,
    ).get_result()

    response = dict(response)
    result_emotions = response["emotion"]["document"]["emotion"]
    return result_emotions
