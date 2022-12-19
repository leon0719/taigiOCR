import cv2
import os
import numpy as np
from PIL import Image

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