
import cv2 as cv2
import numpy as np


cv2.destroyAllWindows()

threshold = 150

cv2.namedWindow('before', cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('after', cv2.WINDOW_KEEPRATIO)

image_name = 'data/calibrated.jpg'
imageCropped_name = 'data/cropped.jpg'

image = cv2.imread(image_name)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(T, thresh) = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

areas = [cv2.contourArea(c) for c in contours]
max_idx = np.argmax(areas)
cnt = contours[max_idx]
rect = cv2.minAreaRect(cnt)

box = cv2.boxPoints(rect)
box = np.int0(box)

cols, rows = image.shape[0:2]

M = cv2.getRotationMatrix2D(rect[0],rect[2]+90,1)
dst = cv2.warpAffine(image,M,(rows, cols))

cv2.imshow('before', dst)

center = np.array(rect[0])
size = np.int0(np.array(rect[1]))
size = np.flip(size,0)
left_down = np.int0(center-size/2)

dst = dst[left_down[1]:left_down[1]+size[1], left_down[0]:left_down[0]+size[0]]

cv2.imshow('after', dst)
cv2.imwrite(imageCropped_name, dst)