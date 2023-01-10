import os
import re

input_file = 'TextRecognitionDataGenerator/trdg/dicts/en/en_article.txt'
line_list = []

with open(input_file,'r',encoding='utf-8') as f :
    for line in f.readlines():
        line = line.strip('\n')
        line = re.sub(r'ぁ|あ|ぃ|い|ぅ|う|ぇ|え|ぉ|お|か|が|き|ぎ|く|ぐ|け|げ|こ|ご|さ|ざ|し|じ|す|ず|せ|ぜ|そ|ぞ|た|だ|ち|ぢ|っ|つ|づ|て|で|と|ど|な|に|ぬ|ね|の|は|ば|ぱ|ひ|び|ぴ|ふ|ぶ|ぷ|へ|べ|ぺ|ほ|ぼ|ぽ|ま|み|む|め|も|ゃ|や|ゅ|ゆ|ょ|よ|ら|り|る|れ|ろ|ゎ|わ|ゐ|を|ん|ゕ|ゖ|ゞ|ァ|ア|ィ|イ|ゥ|ウ|ェ|エ|ォ|オ|カ|ガ|キ|ギ|ク|グ|ケ|ゲ|コ|ゴ|サ|ザ|シ|ジ|ス|ズ|セ|ゼ|ソ|ゾ|タ|ダ|チ|ヂ|ッ|ツ|ヅ|テ|デ|ト|ド|ナ|ニ|ヌ|ネ|ノ|ハ|バ|パ|ヒ|ビ|ピ|フ|ブ|プ|ヘ|ベ|ペ|ホ|ボ|ポ|マ|ミ|ム|メ|モ|ャ|ヤ|ュ|ユ|ョ|ヨ|ラ|リ|ル|レ|ロ|ワ|ヰ|ヱ|ヲ|ン|ヴ|ヵ|ヶ|ー|ヾ|ㄅ|ㄆ|ㄇ|ㄈ|ㄉ|ㄋ|ㄍ|ㄏ|ㄑ|ㄔ|ㄕ|ㄙ|ㄚ|ㄜ|ㄡ|ㄢ|ㄣ|ㄤ|ㄧ|ㄨ|ㆠ|ㆡ|ㆤ|ㆩ|ㆷ|','',line)
        line_list.append(line.replace('    ',' ').replace('   ',' ').replace('  ',' ').replace('　',' ').strip())


with open(input_file,'w',encoding='utf-8') as f:
    for i in line_list:
        f.write(i+'\n')

