import os
img_path = 'test_data/HAN_LO/HAN_LO_img'

for img in os.listdir(img_path):
    os.rename(os.path.join(img_path,img),os.path.join(img_path,img.replace('爱','愛').replace('黄','黃').replace('飮','飲').replace('纯','純').replace('脱','脫')))