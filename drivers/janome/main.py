from janome.tokenizer import Tokenizer

# token.surface, '\t',                  表層形
# token.part_of_speech.split(',')[0],   品詞
# token.part_of_speech.split(',')[1],   品詞細分類1
# token.part_of_speech.split(',')[2],   品詞細分類2
# token.part_of_speech.split(',')[3],   品詞細分類3
# token.infl_type,                      活用型
# token.infl_form,                      活用形
# token.base_form,                      原形
# token.reading,                        読み
# token.phonetic,                       発音

tokenizer = Tokenizer()
