import os
with open('/home/leon/taigiOCR/test_data_extend/Hanji/rec_gt.txt', 'r', encoding='utf8') as f:
    f = f.readlines()
    line_list = [line.strip().split('\t') for line in f]

img_path = '/home/leon/taigiOCR/test_data_extend/Hanji'

count = 1
for line in line_list:
    os.rename(os.path.join(img_path, line[0]), os.path.join(
        img_path, os.path.join('crop_img', line[1].replace('/', ' ').replace(' ', '_')+f'_{count}'+'.jpg')))
    count += 1
