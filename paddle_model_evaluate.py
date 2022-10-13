import os
os.chdir('/workspace/PaddleOCR')
os.system(
    f'python3 tools/infer_rec.py -c configs/rec/PP-OCRv3/multi_language/chinese_cht_PP-OCRv3_rec.yml -o Global.pretrained_model=ch-cht-Pretrained/best_accuracy  Global.infer_img=/workspace/test_data/HAN_LO/HAN_LO_img')
with open('/workspace/PaddleOCR/output/rec/predicts_ppocrv3_chinese_cht.txt', 'r', encoding='utf-8') as f:
    f = f.readlines()
    a = [[' '.join(x.split('/')[-1].split('\t')[0].split('_')[:-1]), x.split('\t')[1]]
         for x in f]

os.chdir('/workspace')
with open('ground_truths.txt', 'w', encoding='utf-8') as f:
    for line in a:
        f.write(line[0]+'\n')

word_list = []
with open('./ground_truths.txt', 'r', encoding='utf-8') as f:
    f = f.readlines()
    for word in f:
        word_list.append(' '.join(word.strip()))

with open('Ground_truths.txt', 'w', encoding='utf-8') as f:
    for line in word_list:
        f.write(line+'\n')

with open('predicts.txt', 'w', encoding='utf-8') as f:
    for line in a:
        f.write(line[1]+'\n')
word_list = []
with open('predicts.txt', 'r', encoding='utf-8') as f:
    f = f.readlines()
    for word in f:
        word_list.append(' '.join(word.strip()))

with open('Predicts.txt', 'w', encoding='utf-8') as f:
    for line in word_list:
        f.write(line+'\n')

os.system(
    f'wer -c Ground_truths.txt Predicts.txt > result_en_confusion_matrix.txt')
os.remove('Ground_truths.txt')
os.remove('Predicts.txt')
