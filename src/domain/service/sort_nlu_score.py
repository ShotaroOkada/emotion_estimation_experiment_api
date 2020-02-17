#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint


# NLUから受け取ったオブェクトをスコアが降順になるように並べ替える
def sort_nlu_score(nlu_score):
    try:
        sorted_score = sorted(
            nlu_score.items(), key=lambda x: x[1], reverse=True)
    except Exception as error:
        print("error sort nlu score: ", error)
    else:
        return sorted_score


if __name__ == '__main__':
    nlu_score = {
        "sadness": 0.203556,
        "joy": 0.140222,
        "fear": 0.064867,
        "disgust": 0.130679,
        "anger": 0.05636
    }

    sorted_score = sort_nlu_score(nlu_score)
    pprint.pprint(sorted_score)
    first_key, first_value = sorted_score[0]
    print(first_key)
    print(first_value)
