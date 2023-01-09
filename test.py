import os
text_path = 'TextRecognitionDataGenerator/trdg/dicts'
text_path_list = []
for r ,d ,f in os.walk(text_path):
    for file in f:
        if file.endswith('.txt') and not file.startswith('jp'):
            text_path_list.append(os.path.join(r,file))
word_list = []
for txt in text_path_list:
    with open(txt,'r',encoding='utf8') as f:
        f = f.readlines()
        for line in f:
            line = line.strip('\n')
            for word in line:
                word_list.append(word)

set_list = sorted(list(set(word_list)))
with open('vocab.txt','w',encoding='utf-8') as f:
    for i in set_list:
        f.write(i+'\n')

