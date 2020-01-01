#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.drivers.nlu.app import natural_language_understanding
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
import json
import pprint


def nlu_estimation_emotion(text):
    try:
        # テキストから感情を推定してもらう
        response = natural_language_understanding.analyze(
            features=Features(emotion=EmotionOptions(targets=None)),
            text=text,
        ).get_result()
    except Exception as error:
        print("error nlu estimation emotion: ", error)
    else:
        response = dict(response)
        result_emotions = response["emotion"]["document"]["emotion"]
        print("success nlu estimation emotion")
        pprint.pprint(result_emotions)
        return result_emotions
