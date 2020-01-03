#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.drivers.janome.app import tokenizer


def morphological_analysis(text):

    words = []
    for token in tokenizer.tokenize(text):
        part = token.part_of_speech.split(',')
        # その単語が接尾&数&非自立以外の名詞　or サ変以外の自立動詞
        if ((part[0] == '名詞' and part[1] != '接尾' and part[1] != '数' and part[1] != '非自立' and token.base_form != '/' and token.base_form != ':')
                or (part[0] == '動詞' and part[1] == '自立' and token.infl_type != 'サ変・スル' and token.base_form != 'ある')
            ):
            words.append(token.base_form)

    print('Morphological analysis results')
    for word in words:
        print(word)

    return words
