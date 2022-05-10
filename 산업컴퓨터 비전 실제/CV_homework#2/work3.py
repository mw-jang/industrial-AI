# 산업컴퓨터 비전 실제 과제
# 3.Panorama
# 2020254007 장민우

import numpy as np
import cv2
import os

path = '.\\data\\'
images = []

for root, directories, files in os.walk(path):

    for file in files:
        if '.jpg' in file:
            img_input = cv2.imread(os.path.join(root, file))
            dst = cv2.resize(img_input, dsize=(640, 480))
            images.append(dst)

stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
status, pano = stitcher.stitch(images)

if status != cv2.Stitcher_OK:
    print("Can't stitch images, error code = %d" % status)
    exit(-1)

cv2.imshow('result', pano)
cv2.waitKey(0)
print("stitching completed successfully.")