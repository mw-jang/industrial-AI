import cv2
import numpy as np
import matplotlib.pylab as plt

kernel = np.ones((7, 7), np.uint8)

# 영상 불러오기
img1 = cv2.imread('data/original.png')
img2 = cv2.imread('data/defect.png')

# BGR 색공간 이미지를 lab 색공간 이미지로 변환
g_o_img = cv2.cvtColor(img1, cv2.COLOR_BGR2LAB)[..., 0]
g_def_img = cv2.cvtColor(img2, cv2.COLOR_BGR2LAB)[..., 0]

# 이미지 연산
sub = cv2.subtract(g_o_img, g_def_img)
thresh = cv2.threshold(sub, 130, 255, cv2.THRESH_BINARY)[1]

# 열림 연산
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Detecting blobs
params = cv2.SimpleBlobDetector_Params()
params.filterByInertia = False
params.filterByConvexity = False
params.filterByCircularity = False

# 부정연산 (not 연산-반대로하기)
im = cv2.bitwise_not(opening)

detector = cv2.SimpleBlobDetector_create(params)

# 키 포인트 검출
keypoints = detector.detect(im)

# 키 포인트에 빨간색 원그리기
im_with_keypoints = cv2.drawKeypoints(img2, keypoints, np.array([]), (0, 0, 255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# 이미지 출력
cv2.imshow('original', img1)
cv2.imshow('detect', img2)
cv2.imshow('image', im_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()