import os
from PIL import Image
from sklearn.model_selection import train_test_split
import shutil
from tqdm import tqdm
import cv2
import numpy as np

# 生成圖片github 路徑
text_gerner = '/workspace/TextRecognitionDataGenerator/trdg'
# 設定訓練資料圖片保存的資料夾的"絕對路徑"
save_img_path = '/train_data/'

# --------------------------------------------------
train_data_path = os.path.join(save_img_path, 'train_data')
train_path = os.path.join(train_data_path, 'train')
vaild_path = os.path.join(train_data_path, 'test')
# --------------------------------------------------
test_en_img_path = os.path.join(save_img_path, 'test_en')
test_ch_img_path = os.path.join(save_img_path, 'test_ch')
test_POJ_img_path = os.path.join(save_img_path, 'test_POJ')
test_TAI_LO_img_path = os.path.join(save_img_path, 'test_TAI_LO')
test_HAN_LO_img_path = os.path.join(save_img_path, 'test_HAN_LO')
test_jp_img_path = os.path.join(save_img_path, 'test_jp')
# ---------------------------------------------------
if not os.path.exists(train_data_path):
    os.makedirs(train_data_path)
if not os.path.exists(train_path):
    os.makedirs(train_path)
if not os.path.exists(vaild_path):
    os.makedirs(vaild_path)

# ---------------------------------------------------


def dilate(img_path, save_en_path):
    for file in os.listdir(img_path):
        image = cv2.imread(os.path.join(img_path, file), 3)
        kernel = np.ones((2, 2), np.uint8)
        dilate = cv2.dilate(image, kernel, iterations=1)
        cv2.imwrite(os.path.join(save_en_path, file), dilate)


def opening(img_path, save_en_path):
    for file in os.listdir(img_path):
        image = cv2.imread(os.path.join(img_path, file), 3)
        kernel = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(
            image, cv2.MORPH_OPEN, kernel=kernel, iterations=1)
        cv2.imwrite(os.path.join(save_en_path, file), opening)


def closing(img_path, save_en_path):
    # 1.enrode 2.dilate
    for file in os.listdir(img_path):
        image = cv2.imread(os.path.join(img_path, file), 3)
        kernel = np.ones((2, 2), np.uint8)
        closing = cv2.morphologyEx(
            image, cv2.MORPH_CLOSE, kernel=kernel, iterations=1)
        cv2.imwrite(os.path.join(save_en_path, file), closing)

# -------------------------------------------------------


def Gerner_en_img():
    data_en_path = os.path.join(save_img_path, 'en')
    if not os.path.exists(data_en_path):
        os.mkdir(data_en_path)
    if not os.path.exists(test_en_img_path):
        os.makedirs(test_en_img_path)

    os.chdir(text_gerner)
    save_img_path1 = f'{save_img_path}/en1'

    print('生成en_img_data')
    os.system(
        f'python run.py  \
            -c 300000 \
            -f 48 \
            -d 3 \
            -i dicts/en/en_article.txt \
            -fd fonts/en/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/en --output_dir {data_en_path}'
    )

    # -----------------------------------------------------------
    save_img_path2 = f'{save_img_path}/en2'
    os.chdir(text_gerner)
    print('生成en_img_data')
    os.system(
        f'python run.py  \
            -c 300000 \
            -f 48 \
            -d 3 \
            -i dicts/en/en_article2.txt \
            -fd fonts/en/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/en --output_dir {save_img_path2}'
    )
    dilate(save_img_path2, data_en_path)

    shutil.rmtree(save_img_path2)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成en_img_data')
    save_img_path3 = f'{save_img_path}/en3'
    os.system(
        f'python run.py  \
            -c 300000 \
            -f 48 \
            -i dicts/en/en_article3.txt \
            -fd fonts/en/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/en --output_dir {save_img_path}/en3'
    )
    closing(save_img_path3, data_en_path)

    shutil.rmtree(save_img_path3)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成en_img_data')
    os.system(
        f'python run.py  \
            -c 300000 \
            -f 48 \
            -i dicts/en/en_article4.txt \
            -fd fonts/en/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/en --output_dir {data_en_path}'
    )
    # -----------------------------------------------------------
    for file in os.listdir(data_en_path):
        os.rename(
            os.path.join(data_en_path, file),
            os.path.join(data_en_path, file.replace(' ', '_'))
        )

    data_en = os.listdir(data_en_path)
    train_en, vaild_en = train_test_split(
        data_en, test_size=0.1, random_state=0)

    Test_en, Vaild_en = train_test_split(
        vaild_en, test_size=0.5, random_state=0)

    print('切割訓練集.....')
    for file in tqdm(train_en):
        shutil.move(os.path.join(data_en_path, file),
                    os.path.join(train_path, file))
    print('切割驗證集.....')
    for file in tqdm(vaild_en):
        shutil.move(os.path.join(data_en_path, file),
                    os.path.join(vaild_path, file))

    for file in tqdm(Test_en[:10000]):
        shutil.copy(os.path.join(vaild_path, file),
                    os.path.join(test_en_img_path, file))
    os.rmdir(data_en_path)


def Gerner_ch_img():
    data_ch_path = os.path.join(save_img_path, 'ch')
    if not os.path.exists(data_ch_path):
        os.mkdir(data_ch_path)
    if not os.path.exists(test_ch_img_path):
        os.makedirs(test_ch_img_path)

    os.chdir(text_gerner)
    print('生成ch_img_data')
    os.system(
        f'python run.py  \
            -c 300000 \
            -f 48 \
            -d 3 \
            -i dicts/ch/ch_article.txt \
            -fd fonts/ch/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/Hanji --output_dir {data_ch_path}'
    )
    # -----------------------------------------------------------
    save_img_path2 = f'{save_img_path}/ch2'
    os.chdir(text_gerner)
    print('生成ch_img_data')
    os.system(
        f'python run.py  \
            -c 300000 \
            -f 48 \
            -d 3 \
            -i dicts/ch/ch_article2.txt \
            -fd fonts/ch/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/Hanji --output_dir {save_img_path2}'
    )

    dilate(save_img_path2, data_ch_path)

    shutil.rmtree(save_img_path2)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成ch_img_data')
    save_img_path3 = f'{save_img_path}/ch3'
    os.system(
        f'python run.py  \
            -c 300000 \
            -f 48 \
            -i dicts/ch/ch_article3.txt \
            -fd fonts/ch/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/Hanji --output_dir {save_img_path3}'
    )
    closing(save_img_path3, data_ch_path)

    shutil.rmtree(save_img_path3)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成ch_img_data')
    os.system(
        f'python run.py  \
            -c 300000 \
            -f 48 \
            -i dicts/ch/ch_article4.txt \
            -fd fonts/ch/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/Hanji --output_dir {data_ch_path}'
    )
    # -----------------------------------------------------------
    for file in os.listdir(data_ch_path):
        os.rename(
            os.path.join(data_ch_path, file),
            os.path.join(data_ch_path, file.replace(' ', '_'))
        )

    data_ch = os.listdir(data_ch_path)
    train_ch, vaild_ch = train_test_split(
        data_ch, test_size=0.1, random_state=0)

    Test_ch, Vaild_ch = train_test_split(
        vaild_ch, test_size=0.5, random_state=0)

    print('切割訓練集.....')
    for file in tqdm(train_ch):
        shutil.move(os.path.join(data_ch_path, file),
                    os.path.join(train_path, file))
    print('切割驗證集.....')
    for file in tqdm(vaild_ch):
        shutil.move(os.path.join(data_ch_path, file),
                    os.path.join(vaild_path, file))

    for file in tqdm(Test_ch[:10000]):
        shutil.copy(os.path.join(vaild_path, file),
                    os.path.join(test_ch_img_path, file))
    os.rmdir(data_ch_path)


def Gerner_POJ_img():
    data_POJ_path = os.path.join(save_img_path, 'POJ')
    if not os.path.exists(data_POJ_path):
        os.mkdir(data_POJ_path)
    if not os.path.exists(test_POJ_img_path):
        os.makedirs(test_POJ_img_path)

    os.chdir(text_gerner)
    print('生成POJ_img_data')
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -d 3 \
            -i dicts/POJ/POJ_corpus.txt \
            -fd fonts/POJ/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/POJ --output_dir {data_POJ_path}'
    )
    # -----------------------------------------------------------
    save_img_path2 = f'{save_img_path}/POJ2'
    os.chdir(text_gerner)
    print('生成POJ_img_data')
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -d 3 \
            -i dicts/POJ/POJ_corpus2.txt \
            -fd fonts/POJ/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/POJ --output_dir {save_img_path2}'
    )

    dilate(save_img_path2, data_POJ_path)

    shutil.rmtree(save_img_path2)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成POJ_img_data')
    save_img_path3 = f'{save_img_path}/POJ3'
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -i dicts/POJ/POJ_corpus3.txt \
            -fd fonts/POJ/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/POJ --output_dir {save_img_path}/POJ3'
    )
    closing(save_img_path3, data_POJ_path)

    shutil.rmtree(save_img_path3)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成POJ_img_data')
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -i dicts/POJ/POJ_corpus4.txt \
            -fd fonts/POJ/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/POJ --output_dir {data_POJ_path}'
    )
    # -----------------------------------------------------------
    for file in os.listdir(data_POJ_path):
        os.rename(
            os.path.join(data_POJ_path, file),
            os.path.join(data_POJ_path, file.replace(' ', '_'))
        )

    data_POJ = os.listdir(data_POJ_path)
    train_POJ, vaild_POJ = train_test_split(
        data_POJ, test_size=0.1, random_state=0)

    Test_POJ, Vaild_POJ = train_test_split(
        vaild_POJ, test_size=0.5, random_state=0)

    print('切割訓練集.....')
    for file in tqdm(train_POJ):
        shutil.move(os.path.join(data_POJ_path, file),
                    os.path.join(train_path, file))
    print('切割驗證集.....')
    for file in tqdm(vaild_POJ):
        shutil.move(os.path.join(data_POJ_path, file),
                    os.path.join(vaild_path, file))

    for file in tqdm(Test_POJ[:10000]):
        shutil.copy(os.path.join(vaild_path, file),
                    os.path.join(test_POJ_img_path, file))
    os.rmdir(data_POJ_path)


def Gerner_TAI_LO_img():
    data_TAI_LO_path = os.path.join(save_img_path, 'TAI_LO')
    if not os.path.exists(data_TAI_LO_path):
        os.mkdir(data_TAI_LO_path)
    if not os.path.exists(test_TAI_LO_img_path):
        os.makedirs(test_TAI_LO_img_path)

    os.chdir(text_gerner)
    print('生成TAI_LO_img_data')
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -d 3 \
            -i dicts/TAI_LO/TAI_LO_corpus.txt \
            -fd fonts/TAI_LO/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/POJ --output_dir {data_TAI_LO_path}'
    )
    # -----------------------------------------------------------
    save_img_path2 = f'{save_img_path}/TAI_LO2'
    os.chdir(text_gerner)
    print('生成TAI_LO_img_data')
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -d 3 \
            -i dicts/TAI_LO/TAI_LO_corpus2.txt \
            -fd fonts/TAI_LO/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/POJ --output_dir {save_img_path2}'
    )

    dilate(save_img_path2, data_TAI_LO_path)

    shutil.rmtree(save_img_path2)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成TAI_LO_img_data')
    save_img_path3 = f'{save_img_path}/TAI_LO3'
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -i dicts/TAI_LO/TAI_LO_corpus3.txt \
            -fd fonts/TAI_LO/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/POJ --output_dir {save_img_path}/TAI_LO3'
    )
    closing(save_img_path3, data_TAI_LO_path)

    shutil.rmtree(save_img_path3)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成TAI_LO_img_data')
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -i dicts/TAI_LO/TAI_LO_corpus4.txt \
            -fd fonts/TAI_LO/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/POJ --output_dir {data_TAI_LO_path}'
    )
    # -----------------------------------------------------------
    for file in os.listdir(data_TAI_LO_path):
        os.rename(
            os.path.join(data_TAI_LO_path, file),
            os.path.join(data_TAI_LO_path, file.replace(' ', '_'))
        )

    data_TAI_LO = os.listdir(data_TAI_LO_path)
    train_TAI_LO, vaild_TAI_LO = train_test_split(
        data_TAI_LO, test_size=0.1, random_state=0)

    Test_TAI_LO, Vaild_TAI_LO = train_test_split(
        vaild_TAI_LO, test_size=0.5, random_state=0)

    print('切割訓練集.....')
    for file in tqdm(train_TAI_LO):
        shutil.move(os.path.join(data_TAI_LO_path, file),
                    os.path.join(train_path, file))
    print('切割驗證集.....')
    for file in tqdm(vaild_TAI_LO):
        shutil.move(os.path.join(data_TAI_LO_path, file),
                    os.path.join(vaild_path, file))

    for file in tqdm(Test_TAI_LO[:10000]):
        shutil.copy(os.path.join(vaild_path, file),
                    os.path.join(test_TAI_LO_img_path, file))
    os.rmdir(data_TAI_LO_path)


def Gerner_HAN_LO_img():
    data_HAN_LO_path = os.path.join(save_img_path, 'HAN_LO')
    if not os.path.exists(data_HAN_LO_path):
        os.mkdir(data_HAN_LO_path)
    if not os.path.exists(test_HAN_LO_img_path):
        os.makedirs(test_HAN_LO_img_path)

    os.chdir(text_gerner)
    print('生成HAN_LO_img_data')
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -d 3 \
            -i dicts/HAN_LO/HAN_LO_corpus.txt \
            -fd fonts/HAN_LO/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/HAN_LO --output_dir {data_HAN_LO_path}'
    )
    # -----------------------------------------------------------
    save_img_path2 = f'{save_img_path}/HAN_LO2'
    os.chdir(text_gerner)
    print('生成HAN_LO_img_data')
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -d 3 \
            -i dicts/HAN_LO/HAN_LO_corpus2.txt \
            -fd fonts/HAN_LO/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/HAN_LO --output_dir {save_img_path2}'
    )

    dilate(save_img_path2, data_HAN_LO_path)

    shutil.rmtree(save_img_path2)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成HAN_LO_img_data')
    save_img_path3 = f'{save_img_path}/HAN_LO3'
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -i dicts/HAN_LO/HAN_LO_corpus3.txt \
            -fd fonts/HAN_LO/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/HAN_LO --output_dir {save_img_path3}'
    )
    closing(save_img_path3, data_HAN_LO_path)

    shutil.rmtree(save_img_path3)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成HAN_LO_img_data')
    os.system(
        f'python run.py  \
            -c 100000 \
            -f 48 \
            -i dicts/HAN_LO/HAN_LO_corpus4.txt \
            -fd fonts/HAN_LO/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/HAN_LO --output_dir {data_HAN_LO_path}'
    )
    # -----------------------------------------------------------
    for file in os.listdir(data_HAN_LO_path):
        os.rename(
            os.path.join(data_HAN_LO_path, file),
            os.path.join(data_HAN_LO_path, file.replace(' ', '_'))
        )

    data_HAN_LO = os.listdir(data_HAN_LO_path)
    train_HAN_LO, vaild_HAN_LO = train_test_split(
        data_HAN_LO, test_size=0.1, random_state=0)

    Test_HAN_LO, Vaild_HAN_LO = train_test_split(
        vaild_HAN_LO, test_size=0.5, random_state=0)

    print('切割訓練集.....')
    for file in tqdm(train_HAN_LO):
        shutil.move(os.path.join(data_HAN_LO_path, file),
                    os.path.join(train_path, file))
    print('切割驗證集.....')
    for file in tqdm(vaild_HAN_LO):
        shutil.move(os.path.join(data_HAN_LO_path, file),
                    os.path.join(vaild_path, file))

    for file in tqdm(Test_HAN_LO[:10000]):
        shutil.copy(os.path.join(vaild_path, file),
                    os.path.join(test_HAN_LO_img_path, file))
    os.rmdir(data_HAN_LO_path)


def Gerner_jp_img():
    data_jp_path = os.path.join(save_img_path, 'jp')
    if not os.path.exists(data_jp_path):
        os.mkdir(data_jp_path)
    if not os.path.exists(test_jp_img_path):
        os.makedirs(test_jp_img_path)

    os.chdir(text_gerner)
    print('生成jp_img_data')
    os.system(
        f'python run.py  \
            -c 80000 \
            -f 48 \
            -d 3 \
            -i dicts/jp/jp_corpus.txt \
            -fd fonts/jp/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/Hanji --output_dir {data_jp_path}'
    )
    # -----------------------------------------------------------
    save_img_path2 = f'{save_img_path}/jp2'
    os.chdir(text_gerner)
    print('生成jp_img_data')
    os.system(
        f'python run.py  \
            -c 80000 \
            -f 48 \
            -d 3 \
            -i dicts/jp/jp_corpus2.txt \
            -fd fonts/jp/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/Hanji --output_dir {save_img_path2}'
    )

    dilate(save_img_path2, data_jp_path)

    shutil.rmtree(save_img_path2)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成jp_img_data')
    save_img_path3 = f'{save_img_path}/jp3'
    os.system(
        f'python run.py  \
            -c 80000 \
            -f 48 \
            -i dicts/jp/jp_corpus3.txt \
            -fd fonts/jp/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/Hanji --output_dir {save_img_path3}'
    )
    closing(save_img_path3, data_jp_path)

    shutil.rmtree(save_img_path3)
    # -----------------------------------------------------------
    os.chdir(text_gerner)
    print('生成jp_img_data')
    os.system(
        f'python run.py  \
            -c 80000 \
            -f 48 \
            -i dicts/jp/jp_corpus4.txt \
            -fd fonts/jp/ \
            -t $(cat /proc/cpuinfo | grep "processor" |  wc -l)\
            -id images/Hanji --output_dir {data_jp_path}'
    )
    # -----------------------------------------------------------
    for file in os.listdir(data_jp_path):
        os.rename(
            os.path.join(data_jp_path, file),
            os.path.join(data_jp_path, file.replace(' ', '_'))
        )

    data_jp = os.listdir(data_jp_path)
    train_jp, vaild_jp = train_test_split(
        data_jp, test_size=0.1, random_state=0)

    Test_jp, Vaild_jp = train_test_split(
        vaild_jp, test_size=0.5, random_state=0)

    print('切割訓練集.....')
    for file in tqdm(train_jp):
        shutil.move(os.path.join(data_jp_path, file),
                    os.path.join(train_path, file))
    print('切割驗證集.....')
    for file in tqdm(vaild_jp):
        shutil.move(os.path.join(data_jp_path, file),
                    os.path.join(vaild_path, file))

    for file in tqdm(Test_jp[:10000]):
        shutil.copy(os.path.join(vaild_path, file),
                    os.path.join(test_jp_img_path, file))
    os.rmdir(data_jp_path)

# ------------------------------------------------------------------------


def Gerner_train_test_label():
    train_label_list = [' '.join(file.split('_')[:-1])
                        for file in os.listdir(train_path)
                        ]

    test_label_list = [' '.join(file.split('_')[:-1])
                       for file in os.listdir(vaild_path)
                       ]
    train_img_path = ['train/'+file for file in os.listdir(train_path)]
    test_img_path = ['test/'+file for file in os.listdir(vaild_path)]

    train_img_path_and_label_combined = sorted(
        list(zip(train_img_path, train_label_list)))
    test_img_path_and_label_combined = sorted(
        list(zip(test_img_path, test_label_list)))

    with open(os.path.join(train_data_path, 'train_label.txt'), 'w', encoding='utf8') as f:
        for line in range(len(train_img_path_and_label_combined)):
            f.write(
                train_img_path_and_label_combined[line][0]+'\t'+train_img_path_and_label_combined[line][1])
            f.write('\n')

    with open(os.path.join(train_data_path, 'test_label.txt'), 'w', encoding='utf8') as f:
        for line in range(len(test_img_path_and_label_combined)):
            f.write(
                test_img_path_and_label_combined[line][0]+'\t'+test_img_path_and_label_combined[line][1])
            f.write('\n')
    print('train_img:', len(os.listdir(train_path)))
    print('test_img:', len(os.listdir(vaild_path)))


def main():
    # 選想要製作資料的語言 不想製作哪個語言可註解掉
    Gerner_en_img()
    Gerner_ch_img()
    Gerner_POJ_img()
    Gerner_TAI_LO_img()
    Gerner_HAN_LO_img()
    Gerner_jp_img()
    # -------------------------
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


if __name__ == '__main__':

    main()
