import os
from sklearn.model_selection import train_test_split
import shutil

#生成圖片github 路徑
text_gerner = '/workspace/TextRecognitionDataGenerator/trdg'
#設定訓練資料圖片保存的資料夾的"絕對路徑"
save_img_path = '/train_data/'

#--------------------------------------------------
train_data_path = os.path.join(save_img_path, 'train_data')
train_path = os.path.join(train_data_path, 'train')
test_path = os.path.join(train_data_path, 'test')
#--------------------------------------------------
test_en_img_path = os.path.join(save_img_path,'test_en')
test_ch_img_path = os.path.join(save_img_path,'test_ch')
test_POJ_img_path = os.path.join(save_img_path,'test_POJ')
test_TAI_LO_img_path = os.path.join(save_img_path,'test_TAI_LO')
test_HAN_LO_img_path = os.path.join(save_img_path,'test_HAN_LO')
test_jp_img_path = os.path.join(save_img_path,'test_jp')
# ---------------------------------------------------
if not os.path.exists(train_data_path):
    os.makedirs(train_data_path)
if not os.path.exists(train_path):
    os.makedirs(train_path)
if not os.path.exists(test_path):
    os.makedirs(test_path)
#---------------------------------------------------
def Gerner_en_img():
    os.chdir(text_gerner)
    print('生成en_img_data')
    #參數 -c 圖片數量 -i 語料庫 -fd 字型資料夾 -b 背景圖片 -t cpu核心數(可加快生成圖片速度) -d 加入扭曲雜訊 -f 圖片大小 (預設是32) --output_dir 圖片保存資料夾路徑
    os.system(f'python run.py  -c 2500 -i dicts/en/en_article.txt -fd fonts/train_font/en/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) --character_spacing 3 -b 3 --output_dir {save_img_path}/en')
    os.system(f'python run.py  -c 2500 -i dicts/en/en_article2.txt -fd fonts/train_font/en/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -d 3 -f 48 -b 3 --output_dir {save_img_path}/en')
    os.system(f'python run.py  -c 2500 -i dicts/en/en_article3.txt -fd fonts/train_font/en/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 -b 3 -k 3 -rk --output_dir {save_img_path}/en')
    os.system(f'python run.py  -c 2500 -i dicts/en/en_article4.txt -fd fonts/train_font/en/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 -b 3 -bl 2 -rbl --output_dir {save_img_path}/en')

    en_img_path = os.path.join(save_img_path,'en')
    for file in os.listdir(en_img_path):
        os.rename(
        os.path.join(en_img_path, file),
        os.path.join(en_img_path, file.replace(' ', '_'))
        )
    data_en = os.listdir(en_img_path)
    train_en, test_en = train_test_split(data_en, test_size=0.1, random_state=0)
    print('切割訓練驗證.....')
    for file in train_en:
        shutil.move(os.path.join(en_img_path, file),
                os.path.join(train_path, file))
    for file in test_en:
        shutil.move(os.path.join(en_img_path, file),
                os.path.join(test_path, file))
    os.rmdir(en_img_path)
    os.system(f'python run.py  -c 1000 -i dicts/en/en_article.txt -fd fonts/test_font/en/ -b 3 -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 --output_dir {test_en_img_path}')
    for file in os.listdir(test_en_img_path):
        os.rename(
        os.path.join(test_en_img_path, file),
        os.path.join(test_en_img_path, file.replace(' ', '_'))
                )
def Gerner_ch_img():
    os.chdir(text_gerner)
    print('生成ch_img_data')
    #參數 -c 圖片數量 -l 語料庫 -fd 字型資料夾 -b 背景圖片 -t cpu核心數(可加快生成圖片速度) -d 加入扭曲雜訊 -f 圖片大小 (預設是32) --output_dir 圖片保存資料夾路徑
    os.system(f'python run.py  -c 2000 -i dicts/ch/chinese_article.txt -fd fonts/train_font/ch/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) --character_spacing 3 -b 3 --output_dir {save_img_path}/ch')
    os.system(f'python run.py  -c 2000 -i dicts/ch/chinese_article2.txt -fd fonts/train_font/ch/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -d 3 -f 48 -b 3 --output_dir {save_img_path}/ch')
    os.system(f'python run.py  -c 2000 -i dicts/ch/chinese_article3.txt -fd fonts/train_font/ch/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -b 3 -f 48 -k 3 -rk --output_dir {save_img_path}/ch')
    os.system(f'python run.py  -c 2000 -i dicts/ch/chinese_article4.txt -fd fonts/train_font/ch/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -b 3 -f 48 -bl 2 -rbl --output_dir {save_img_path}/ch')
    os.system(f'python run.py  -c 2000 -i dicts/ch/chinese_article5.txt -fd fonts/train_font/ch/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -b 3 -f 48 --output_dir {save_img_path}/ch')
    ch_img_path = os.path.join(save_img_path,'ch')
    for file in os.listdir(ch_img_path):
        os.rename(
        os.path.join(ch_img_path, file),
        os.path.join(ch_img_path, file.replace(' ', '_'))
                )
    data_ch = os.listdir(ch_img_path)
    train_ch, test_ch = train_test_split(data_ch, test_size=0.1, random_state=0)
    print('切割訓練驗證.....')
    for file in train_ch:
        shutil.move(os.path.join(ch_img_path, file),
                os.path.join(train_path, file))
    for file in test_ch:
        shutil.move(os.path.join(ch_img_path, file),
                os.path.join(test_path, file))
    os.rmdir(ch_img_path)
    os.system(f'python run.py  -c 1000 -i dicts/ch/chinese_article.txt -fd fonts/test_font/ch/ -b 3 -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 --output_dir {test_ch_img_path}')
    for file in os.listdir(test_ch_img_path):
        os.rename(
        os.path.join(test_ch_img_path, file),
        os.path.join(test_ch_img_path, file.replace(' ', '_'))
                )
def Gerner_POJ_img():
    os.chdir(text_gerner)
    print('生成POJ_img_data')
    #參數 -c 圖片數量 -l 語料庫 -fd 字型資料夾 -b 背景圖片 -t cpu核心數(可加快生成圖片速度) -d 加入扭曲雜訊 -f 圖片大小 (預設是32) --output_dir 圖片保存資料夾路徑
    os.system(f'python run.py  -c 2500 -i dicts/POJ/POJ_corpus.txt -fd fonts/train_font/POJ/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) --character_spacing 3 -b 3 --output_dir {save_img_path}/POJ')
    os.system(f'python run.py  -c 2500 -i dicts/POJ/POJ_corpus2.txt -fd fonts/train_font/POJ/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 -b 3 --output_dir {save_img_path}/POJ')
    os.system(f'python run.py  -c 2500 -i dicts/POJ/POJ_corpus3.txt -fd fonts/train_font/POJ/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -d 3 -f 48 -b 3 -k 3 -rk --output_dir {save_img_path}/POJ')
    os.system(f'python run.py  -c 2500 -i dicts/POJ/POJ_corpus4.txt -fd fonts/train_font/POJ/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 -b 3 -bl 2 -rbl --output_dir {save_img_path}/POJ')
    POJ_img_path = os.path.join(save_img_path,'POJ')
    for file in os.listdir(POJ_img_path):
        os.rename(
        os.path.join(POJ_img_path, file),
        os.path.join(POJ_img_path, file.replace(' ', '_'))
                )
    data_POJ = os.listdir(POJ_img_path)
    train_POJ, test_POJ = train_test_split(data_POJ, test_size=0.1, random_state=0)
    print('切割訓練驗證.....')
    for file in train_POJ:
        shutil.move(os.path.join(POJ_img_path, file),
                os.path.join(train_path, file))
    for file in test_POJ:
        shutil.move(os.path.join(POJ_img_path, file),
                os.path.join(test_path, file))
    os.rmdir(POJ_img_path)
    os.system(f'python run.py  -c 1000 -i dicts/POJ/POJ_corpus.txt -fd fonts/test_font/POJ/ -b 3 -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 --output_dir {test_POJ_img_path}')
    for file in os.listdir(test_POJ_img_path):
        os.rename(
        os.path.join(test_POJ_img_path, file),
        os.path.join(test_POJ_img_path, file.replace(' ', '_'))
                )
def Gerner_TAI_LO_img():
    os.chdir(text_gerner)
    print('生成TAI_LO_img_data')
    #參數 -c 圖片數量 -l 語料庫 -fd 字型資料夾 -b 背景圖片 -t cpu核心數(可加快生成圖片速度) -d 加入扭曲雜訊 -f 圖片大小 (預設是32) --output_dir 圖片保存資料夾路徑
    os.system(f'python run.py  -c 2500 -i dicts/TAI_LO/TAI_LO_corpus.txt -fd fonts/train_font/TAI_LO/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) --character_spacing 3 -b 3 --output_dir {save_img_path}/TAI_LO')
    os.system(f'python run.py  -c 2500 -i dicts/TAI_LO/TAI_LO_corpus2.txt -fd fonts/train_font/TAI_LO/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -d 3 -f 48 -b 3 --output_dir {save_img_path}/TAI_LO')
    os.system(f'python run.py  -c 2500 -i dicts/TAI_LO/TAI_LO_corpus3.txt -fd fonts/train_font/TAI_LO/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 -b 3 -k 3 -rk --output_dir {save_img_path}/TAI_LO')
    os.system(f'python run.py  -c 2500 -i dicts/TAI_LO/TAI_LO_corpus4.txt -fd fonts/train_font/TAI_LO/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -b 3 -f 48 -bl 2 -rbl --output_dir {save_img_path}/TAI_LO')
    TAI_LO_img_path = os.path.join(save_img_path,'TAI_LO')
    for file in os.listdir(TAI_LO_img_path):
        os.rename(
        os.path.join(TAI_LO_img_path, file),
        os.path.join(TAI_LO_img_path, file.replace(' ', '_'))
                )
    data_TAI_LO = os.listdir(TAI_LO_img_path)
    train_TAI_LO, test_TAI_LO = train_test_split(data_TAI_LO, test_size=0.1, random_state=0)
    print('切割訓練驗證.....')
    for file in train_TAI_LO:
        shutil.move(os.path.join(TAI_LO_img_path, file),
                os.path.join(train_path, file))
    for file in test_TAI_LO:
        shutil.move(os.path.join(TAI_LO_img_path, file),
                os.path.join(test_path, file))
    os.rmdir(TAI_LO_img_path)
    os.system(f'python run.py  -c 1000 -i dicts/TAI_LO/TAI_LO_corpus.txt -fd fonts/test_font/TAI_LO/ -b 3 -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 --output_dir {test_TAI_LO_img_path}')
    for file in os.listdir(test_TAI_LO_img_path):
        os.rename(
        os.path.join(test_TAI_LO_img_path, file),
        os.path.join(test_TAI_LO_img_path, file.replace(' ', '_'))
                )
def Gerner_HAN_LO_img():
    os.chdir(text_gerner)
    print('生成HAN_LO_img_data')
    #參數 -c 圖片數量 -l 語料庫 -fd 字型資料夾 -b 背景圖片 -t cpu核心數(可加快生成圖片速度) -d 加入扭曲雜訊 -f 圖片大小 (預設是32) --output_dir 圖片保存資料夾路徑 -k 傾斜角度 -rk 隨機傾斜
    os.system(f'python run.py  -c 2500 -i dicts/HAN_LO/HAN_LO_corpus.txt -fd fonts/train_font/HAN_LO/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) --character_spacing 3 -b 3 --output_dir {save_img_path}/HAN_LO')
    os.system(f'python run.py  -c 2500 -i dicts/HAN_LO/HAN_LO_corpus2.txt -fd fonts/train_font/HAN_LO/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -d 3 -f 48 -b 3 --output_dir {save_img_path}/HAN_LO')
    os.system(f'python run.py  -c 2500 -i dicts/HAN_LO/HAN_LO_corpus3.txt -fd fonts/train_font/HAN_LO/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -b 3 -f 48 -k 3 -rk --output_dir {save_img_path}/HAN_LO')
    os.system(f'python run.py  -c 2500 -i dicts/HAN_LO/HAN_LO_corpus4.txt -fd fonts/train_font/HAN_LO/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -b 3 -f 48 -bl 2 -rbl --output_dir {save_img_path}/HAN_LO')
    HAN_LO_img_path = os.path.join(save_img_path,'HAN_LO')
    for file in os.listdir(HAN_LO_img_path):
        os.rename(
        os.path.join(HAN_LO_img_path, file),
        os.path.join(HAN_LO_img_path, file.replace(' ', '_'))
                )
    data_HAN_LO = os.listdir(HAN_LO_img_path)
    train_HAN_LO, test_HAN_LO = train_test_split(data_HAN_LO, test_size=0.1, random_state=0)
    print('切割訓練驗證.....')
    for file in train_HAN_LO:
        shutil.move(os.path.join(HAN_LO_img_path, file),
                os.path.join(train_path, file))
    for file in test_HAN_LO:
        shutil.move(os.path.join(HAN_LO_img_path, file),
                os.path.join(test_path, file))
    os.rmdir(HAN_LO_img_path)
    os.system(f'python run.py  -c 1000 -i dicts/HAN_LO/HAN_LO_corpus.txt -fd fonts/test_font/HAN_LO/ -b 3 -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 --output_dir {test_HAN_LO_img_path}')
    for file in os.listdir(test_HAN_LO_img_path):
        os.rename(
        os.path.join(test_HAN_LO_img_path, file),
        os.path.join(test_HAN_LO_img_path, file.replace(' ', '_'))
                )
def Gerner_jp_img():
    os.chdir(text_gerner)
    print('生成jp_img_data')
    #參數 -c 圖片數量 -l 語料庫 -fd 字型資料夾 -b 背景圖片 -t cpu核心數(可加快生成圖片速度) -d 加入扭曲雜訊 -f 圖片大小 (預設是32) --output_dir 圖片保存資料夾路徑
    os.system(f'python run.py  -c 2500 -i dicts/jp/jp_corpus.txt -fd fonts/train_font/jp/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) --character_spacing 3 -b 3 --output_dir {save_img_path}/jp')
    os.system(f'python run.py  -c 2500 -i dicts/jp/jp_corpus2.txt -fd fonts/train_font/jp/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -d 3 -f 48 -b 3 --output_dir {save_img_path}/jp')
    os.system(f'python run.py  -c 2500 -i dicts/jp/jp_corpus3.txt -fd fonts/train_font/jp/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -b 3 -f 48 -k 3 -rk --output_dir {save_img_path}/jp')
    os.system(f'python run.py  -c 2500 -i dicts/jp/jp_corpus4.txt -fd fonts/train_font/jp/ -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -b 3 -f 48 -bl 2 -rbl --output_dir {save_img_path}/jp')
    jp_img_path = os.path.join(save_img_path,'jp')
    for file in os.listdir(jp_img_path):
        os.rename(
        os.path.join(jp_img_path, file),
        os.path.join(jp_img_path, file.replace(' ', '_'))
                )
    data_jp = os.listdir(jp_img_path)
    train_jp, test_jp = train_test_split(data_jp, test_size=0.1, random_state=0)
    print('切割訓練驗證.....')
    for file in train_jp:
        shutil.move(os.path.join(jp_img_path, file),
                os.path.join(train_path, file))
    for file in test_jp:
        shutil.move(os.path.join(jp_img_path, file),
                os.path.join(test_path, file))
    os.rmdir(jp_img_path)
    os.system(f'python run.py  -c 1000 -i dicts/jp/jp_corpus.txt -fd fonts/test_font/jp/ -b 3 -t $(cat /proc/cpuinfo | grep "processor" |  wc -l) -f 48 --output_dir {test_jp_img_path}')
    for file in os.listdir(test_jp_img_path):
        os.rename(
        os.path.join(test_jp_img_path, file),
        os.path.join(test_jp_img_path, file.replace(' ', '_'))
                )
# ------------------------------------------------------------------------
def Gerner_train_test_label():
    train_label_list=[' '.join(file.split('_')[:-1])
                     for file in os.listdir(train_path)
                     ]

    test_label_list =[' '.join(file.split('_')[:-1])
                     for file in os.listdir(test_path)
                     ]
    train_img_path=['train/'+file for file in os.listdir(train_path)]
    test_img_path=['test/'+file for file in os.listdir(test_path)]

    train_img_path_and_label_combined = sorted(list(zip(train_img_path, train_label_list)))
    test_img_path_and_label_combined = sorted(list(zip(test_img_path, test_label_list)))

    with open(os.path.join(train_data_path, 'train_label.txt'), 'w', encoding='utf8') as f:
        for line in range(len(train_img_path_and_label_combined)):
            f.write(train_img_path_and_label_combined[line][0]+'\t'+train_img_path_and_label_combined[line][1])
            f.write('\n')

    with open(os.path.join(train_data_path, 'test_label.txt'), 'w', encoding='utf8') as f:
        for line in range(len(test_img_path_and_label_combined)):
            f.write(test_img_path_and_label_combined[line][0]+'\t'+test_img_path_and_label_combined[line][1])
            f.write('\n')
    print('train_img:', len(os.listdir(train_path)))
    print('test_img:', len(os.listdir(test_path)))

if __name__ == '__main__':
    #選想要製作資料的語言 不想製作哪個語言可註解掉
    Gerner_en_img()
    Gerner_ch_img()
    Gerner_POJ_img()
    Gerner_TAI_LO_img()
    Gerner_HAN_LO_img()
    Gerner_jp_img()
    #-------------------------
    Gerner_train_test_label()

    '''
    執行後資料夾樹狀圖
    save_img_path/
    ├── test_ch
    ├── test_en
    ├── test_HAN_LO
    ├── test_jp
    ├── test_POJ
    ├── test_TAI_LO
    └── train_data
        ├── test
        ├── test_label.txt
        ├── train
        └── train_label.txt
    '''

