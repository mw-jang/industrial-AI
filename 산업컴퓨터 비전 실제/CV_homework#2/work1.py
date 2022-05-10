#산업컴퓨터 비전 실제 과제
#1.Feature Detection
#2020254007 장민우

import sys
import cv2
import numpy as np
import matplotlib.pylab as plt

def canny():
    # 이미지 읽기
    img1 = cv2.imread('data/boat1.jpg')
    img2 = cv2.imread('data/budapest1.jpg')
    img3 = cv2.imread('data/newspaper1.jpg')
    img4 = cv2.imread('data/s1.jpg')

    dst1 = cv2.resize(img1, dsize=(640, 480))
    dst2 = cv2.resize(img2, dsize=(640, 480))
    dst3 = cv2.resize(img3, dsize=(640, 480))
    dst4 = cv2.resize(img4, dsize=(640, 480))

    edge1 = cv2.Canny(dst1, 50, 200)
    edge2 = cv2.Canny(dst2, 100, 200)
    edge3 = cv2.Canny(dst3, 130, 200)
    edge4 = cv2.Canny(dst4, 170, 200)

    cv2.imshow('img1 Edge', edge1)
    cv2.imshow('img2 Edge', edge2)
    cv2.imshow('img3 Edge', edge3)
    cv2.imshow('img4 Edge', edge4)

def harris():
    # 이미지 읽기
    img1 = cv2.imread('data/boat1.jpg')
    img2 = cv2.imread('data/budapest1.jpg')
    img3 = cv2.imread('data/newspaper1.jpg')
    img4 = cv2.imread('data/s1.jpg')

    reimg1 = cv2.resize(img1, dsize=(640, 480))
    reimg2 = cv2.resize(img2, dsize=(640, 480))
    reimg3 = cv2.resize(img3, dsize=(640, 480))
    reimg4 = cv2.resize(img4, dsize=(640, 480))

    gray1 = cv2.cvtColor(reimg1, cv2.COLOR_BGR2GRAY)
    gray1 = np.float32(gray1)
    dst1 = cv2.cornerHarris(gray1, 2, 3, 0.04)
    reimg1[dst1 > 0.01 * dst1.max()] = [0, 0, 255]

    gray2 = cv2.cvtColor(reimg2, cv2.COLOR_BGR2GRAY)
    gray2 = np.float32(gray2)
    dst2 = cv2.cornerHarris(gray2, 2, 3, 0.05)
    reimg1[dst2 > 0.01 * dst2.max()] = [0, 0, 255]

    gray3 = cv2.cvtColor(reimg3, cv2.COLOR_BGR2GRAY)
    gra3 = np.float32(gray3)
    dst3 = cv2.cornerHarris(gray3, 2, 3, 0.04)
    reimg1[dst3 > 0.01 * dst3.max()] = [0, 0, 255]

    gray4 = cv2.cvtColor(reimg4, cv2.COLOR_BGR2GRAY)
    gray4 = np.float32(gray4)
    dst4 = cv2.cornerHarris(gray4, 2, 3, 0.05)
    reimg1[dst4 > 0.01 * dst4.max()] = [0, 0, 255]

    cv2.imshow('dst1', reimg1)
    cv2.imshow('dst2', reimg2)
    cv2.imshow('dst3', reimg3)
    cv2.imshow('dst4', reimg4)


canny()
harris()

cv2.waitKey(0)
cv2.destroyAllWindows