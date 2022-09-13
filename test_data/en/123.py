with open('/home/leon/taigiOCR/test_data/Hanji/rec_gt.txt', 'r', encoding='utf-8') as f:

    f = f.readlines()

    txt_list = [line.strip().split('\t')[1] for line in f]


with open('Hanji.txt', 'w', encoding='utf-8') as f:
    for line in txt_list:
        f.write(line+'\n')
