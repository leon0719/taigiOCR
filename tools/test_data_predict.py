import os

language = [line[5:] for line in os.listdir('/train_data') if line.startswith('test') ]

for lang in language:
    os.chdir('/workspace/PaddleOCR')
    if not os.path.exists(f'result_{lang}'):
        os.mkdir(f'result_{lang}')
    os.system(f'python3 tools/infer_rec.py -c configs/rec/PP-OCRv3/PP-OCRv3_rec.yml -o Global.pretrained_model=output/my_ocr_model/best_accuracy  Global.infer_img=/train_data/test_{lang}')
    with open('/workspace/PaddleOCR/output/rec/predicts_my_ocr_model.txt','r',encoding='utf-8') as f :
        f=f.readlines()
        select_word_list = [line.strip().split('/')[3][:-18] for line in f]
    os.chdir(f'/workspace/PaddleOCR/result_{lang}')
    with open('ground_truths_and_predicts.txt','w',encoding='utf-8') as f :
        for line in select_word_list:
            f.write(line+'\n')
    with open(os.path.join('./','ground_truths_and_predicts.txt'),'r',encoding='utf-8') as f :
        f = f.readlines()
        split_truth_predict = [line.strip('\n').replace('\t',' ').split('.jpg ') for line in f]
        ground_truths = [' '.join(line[0].replace('_',' ').split(' ')[:-1]) for line in split_truth_predict ]
        predicts = [' '.join(line.strip('\n').split('.jpg\t')[1:]) for line in f ]
#-----------------------------------------------------------------
    with open('ground_truths.txt','w',encoding='utf-8') as f :
        for line in ground_truths:
            f.write(line+'\n')
    word_list = []
    with open('./ground_truths.txt','r',encoding='utf-8') as f:
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
# ----------------------------------------------------------------
    os.remove('ground_truths_and_predicts.txt')
    os.system(f'wer -c Ground_truths.txt Predicts.txt > result_{lang}_confusion_matrix.txt' )
    os.remove('Ground_truths.txt')
    os.remove('Predicts.txt')