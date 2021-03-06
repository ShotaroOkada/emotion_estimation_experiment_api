#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class EmotionStrength(Enum):
    LOW = "low"
    MID = "mid"
    HIGH = "high"


class EmotionCategory(Enum):
    ANGER = "anger"
    JOY = "joy"
    SADNESS = "sadness"
    FEAR = "fear"
    DISGUST = "disgust"


order_emotion_category = [EmotionCategory.ANGER.value, EmotionCategory.JOY.value,
                          EmotionCategory.SADNESS.value, EmotionCategory.FEAR.value, EmotionCategory.DISGUST.value]
