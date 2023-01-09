import os
import re
text_path = 'TextRecognitionDataGenerator/trdg/dicts/ch/ch_article.txt'

lines = []

with open(text_path,'r',encoding='utf-8') as f:
    f = f.readlines()
    for line in f:
        line = line.strip('\n')
        line = re.sub(r'[♪〇ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐをんゕゖゞァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロワヰヱヲンヴヵヶーヾㄅㄆㄇㄈㄉㄋㄍㄏㄑㄔㄕㄙㄚㄜㄡㄢㄣㄤㄧㄨㆠㆡㆤㆩㆷ]','',line)
        lines.append(line.replace('    ',' ').replace('   ',' ').replace('  ',' ').replace('　',' '))

with open(text_path,'w',encoding='utf-8') as f:
    for line in lines:
        f.write(line+'\n')

# word_list = []
# for txt in text_path_list:
#     with open(txt,'r',encoding='utf-8') as f:
#         f = f.readlines()
#         for line in f:
#             line = line.strip('\n')
#             for word in line:
#                 word_list.append(word)

# set_list = sorted(list(set(word_list)))
# with open('vocab.txt','w',encoding='utf-8') as f:
#     for i in set_list:
#         f.write(i+'\n')
