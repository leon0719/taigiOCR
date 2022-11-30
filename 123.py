import os

path = '/home/leon/taigiOCR/test_data/HAN_LO/HAN_LO_img'
for i in os.listdir(path):
    os.rename(os.path.join(path,i),os.path.join(path,i.replace('丶','、')))