# 산업 컴퓨터 비전 실제 과제 2.공간 도메인 필터링
# 2020254007 장민우

import cv2
import numpy as np

img = cv2.imread('data/lena.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blr = cv2.GaussianBlur(gray, (0, 0), 2)
dst1 = np.clip(2.0 * gray - blr, 0, 255).astype(np.uint8)

diameter = -1
SigmaColor = 10
SigmaSpace = 5

cv2.imshow("original", gray)

# cv2.bilateralFilter(src, d sigmaColor, sigmaSpace, dst=None, borderType=None) -> dst
# src : 입력 영상. 8비트 또는 실수형, 1채널 또는 3채널.
# d: 필터링에 사용될 이웃 픽셀의 거리(지름). 음수(-1)를 입력하면 sigmaSpace 값에 의해 자동 결정됨.
# sigmaColor : 색 공간에서 필터의 표준 편차
# sigmaSpace : 좌표 공간에서 필터의 표준 편차
# dst : 출력 영상. src와 같은 크기, 같은 타입.
# borderType : 가장자리 픽셀 처리 방식

finish = False
while not finish:
    dst2 = cv2.bilateralFilter(dst1, diameter, SigmaColor, SigmaSpace)
    cv2.imshow('dst1', dst1)
    cv2.imshow("dst2", dst2)
    key = cv2.waitKey(0)

    print('diameter : %d, SigmaColor : %d, SigmaSpace = %d' % (diameter, SigmaColor, SigmaSpace))

    if key == ord('q'):
        diameter = diameter + 1
    elif key == ord('w'):
        diameter = diameter - 1
    elif key == ord('a'):
        SigmaColor = SigmaColor + 1
    elif key == ord('s'):
        SigmaColor = SigmaColor - 1
    elif key == ord('z'):
        SigmaSpace = SigmaSpace + 1
    elif key == ord('x'):
        SigmaSpace = SigmaSpace - 1
    elif key == 27:
        finish = True

cv2.destroyAllWindows()
