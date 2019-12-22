from src.drivers.translator.app import translator


def translate_english(japanese_text):
    trans_en = translator.translate(japanese_text)
    print(trans_en.text)
    return trans_en.text
