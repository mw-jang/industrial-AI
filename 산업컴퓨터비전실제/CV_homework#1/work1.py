#산업컴퓨터 비전 실제 과제
#1.히스토그램 평탄화
#2020254007 장민우

import sys
import cv2
import numpy as np
import matplotlib.pylab as plt

#이미지 읽기
img = cv2.imread('data/House256rgb.png')

if img is None:
    print('Image load failed!')
    sys.exit()

#3채널 히스토그램 계산 및 그리기
channels = cv2.split(img)
colors = ('b', 'g', 'r')
for (ch, color) in zip (channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
plt.show()

#사용자로부터 R,G,B 채널 입력받기
while True:
    print('Press Keyboard b,r,g')
    cv2.imshow('Before', img)
    key = cv2.waitKey(0)

    if key == ord('b'):
        # 히스토그램 계산 및 그리기
        channels = cv2.split(img)
        hist = cv2.calcHist(channels, [0], None, [256], [0, 256])
        plt.plot(hist, color = 'b')
        plt.show()

        # 평탄화 후 영상출력
        # 컬러 스케일 BGR -> YUV
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        # YUV 컬러 스케일의 첫번째 채널에 대해서 이퀄라이즈 적용
        img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

        # 컬러 스케일 YUV -> BGR
        img2 = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        break

    elif key == ord('r'):
        # 히스토그램 계산 및 그리기
        channels = cv2.split(img)
        hist = cv2.calcHist(channels, [1], None, [256], [0, 256])
        plt.plot(hist, color = 'r')
        plt.show()

        # 평탄화 후 영상출력
        # 컬러 스케일 BGR -> YUV
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        # YUV 컬러 스케일의 두번째 채널에 대해서 이퀄라이즈 적용
        img_yuv[:, :, 1] = cv2.equalizeHist(img_yuv[:, :, 1])

        # 컬러 스케일 YUV -> BGR
        img2 = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        break

    elif key == ord('g'):
        # 히스토그램 계산 및 그리기
        channels = cv2.split(img)
        hist = cv2.calcHist(channels, [2], None, [256], [0, 256])
        plt.plot(hist, color = 'g')
        plt.show()

        # 평탄화 후 영상출력
        # 컬러 스케일 BGR -> YUV
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        # YUV 컬러 스케일의 세번째 채널에 대해서 이퀄라이즈 적용
        img_yuv[:, :, 2] = cv2.equalizeHist(img_yuv[:, :, 2])

        # 컬러 스케일 YUV -> BGR
        img2 = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        break

cv2.imshow('After', img2)
cv2.waitKey()
cv2.destroyAllWindows()