import os
path = '/home/leon/Paper_work/PaddleOCR/output/rec/predicts_my_ocr_model.txt'

with open(path,'r',encoding='utf-8') as f :
    f = f.readlines()
    groud_truths = [line.strip().split('\t')[0].split('/')[-1].split('_')[0] for line in f]
    predicts = [line.strip().split('\t')[1] for line in f]


with open('ground_truths.txt','w',encoding='utf-8') as f :
    for line in groud_truths:
        f.write(line.replace('_', ' ')+ '\n')

word_list = []
with open('ground_truths.txt','r',encoding='utf-8') as f:
    f = f.readlines()
    for word in f :
        word_list.append(' '.join(word.strip()))

with open('Ground_truths.txt','w',encoding='utf-8') as f :
    for line in word_list:
        f.write(line+'\n')
# --------------------------------------------------------------

with open('predicts.txt','w',encoding='utf-8') as f :
    for line in predicts:
        f.write(line+'\n')

word_list = []
with open('predicts.txt','r',encoding='utf-8') as f:
    f = f.readlines()
    for word in f :
        word_list.append(' '.join(word.strip()))

with open('Predicts.txt','w',encoding='utf-8') as f :
    for line in word_list:
        f.write(line+'\n')

os.remove('predicts.txt')
os.remove('ground_truths.txt')