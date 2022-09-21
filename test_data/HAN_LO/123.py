import pandas as pd

data = pd.read_excel('rec_gt.xlsx')

with open('rec_gt.txt', 'w', encoding='utf-8') as f:
    for line in range(len(data)):
        f.write(data['img_path'][line]+'\t'+str(data['label'][line])+'\n')
