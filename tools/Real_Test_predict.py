import os

test_ch_img_path = '/workspace/test_data/Hanji/Hanji_img'
test_en_img_path = '/workspace/test_data/en/en_img'
# test_HAN_LO_img_path = '/workspace/test_data/HAN_LO/HAN_LO_img'
# test_POJ_img_path = '/workspace/test_data/POJ/POJ_img'

conbined_list = [test_ch_img_path, test_en_img_path]

if not os.path.exists('real_test_results'):
    os.mkdir('real_test_results')

# ------------------------------------------------------------

for lang in conbined_list:

    os.chdir('/workspace/PaddleOCR')
    os.system(
        f'python3 tools/infer_rec.py -c configs/rec/PP-OCRv3/PP-OCRv3_rec.yml -o Global.pretrained_model=output/my_ocr_model/best_accuracy  Global.infer_img={lang}')
    path = '/workspace/PaddleOCR/output/rec/predicts_my_ocr_model.txt'
    # python3 tools/infer_rec.py -c configs/rec/PP-OCRv3/PP-OCRv3_rec.yml -o Global.pretrained_model=output/my_ocr_model/best_accuracy  Global.infer_img=/test_data/ch/crop/
    with open(path, 'r', encoding='utf-8') as f:
        f = f.readlines()
        groud_truths = [line.strip().split('\t')[0].split(
            '/')[-1].split('_')[:-1] for line in f]
        predicts = [line.strip().split('\t')[1] for line in f]
    lang_dir = lang.split('/')[-1].split('_')[0]

    save_result_path = f'/workspace/tools/real_test_results/{lang_dir}'

    if not os.path.exists(save_result_path):
        os.mkdir(save_result_path)

    os.chdir(save_result_path)
    with open('ground_truths.txt', 'w', encoding='utf-8') as f:
        for line in groud_truths:
            f.write(' '.join(line) + '\n')

    word_list = []
    with open('ground_truths.txt', 'r', encoding='utf-8') as f:
        f = f.readlines()
        for word in f:
            word_list.append(' '.join(word.strip()))

    with open('Ground_truths.txt', 'w', encoding='utf-8') as f:
        for line in word_list:
            f.write(line+'\n')
    # --------------------------------------------------------------

    with open('predicts.txt', 'w', encoding='utf-8') as f:
        for line in predicts:
            f.write(line+'\n')

    word_list = []
    with open('predicts.txt', 'r', encoding='utf-8') as f:
        f = f.readlines()
        for word in f:
            word_list.append(' '.join(word.strip()))

    with open('Predicts.txt', 'w', encoding='utf-8') as f:
        for line in word_list:
            f.write(line+'\n')

    os.system('wer -c Ground_truths.txt Predicts.txt > result_confusion_matrix.txt')
    os.remove('Ground_truths.txt')
    os.remove('Predicts.txt')
