from drivers.translator.main import translator


def translate_english(text):
    trans_en = translator.translate(text)
    print(trans_en.text)
    return trans_en.text
