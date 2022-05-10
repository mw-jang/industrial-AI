import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

img0 = cv2.imread('data/Lena.png')
M = np.array([[math.cos(np.pi/12), -math.sin(np.pi/12), 0],
             [math.sin(np.pi/12), math.cos(np.pi/12), 0],
             [0,0,1]])
Moff = np.eye(3)
Moff[0,2] = -img0.shape[1]/2
Moff[1,2] = -img0.shape[0]/2
print(np.linalg.inv(Moff)@M@Moff)
img1 = cv2.warpPerspective(img0, np.linalg.inv(Moff)@M@Moff,
                           (img0.shape[1], img0.shape[0]), borderMode=cv2.BORDER_REPLICATE)
cv2.imwrite('data/Lena_rotated.png', img1)

img0 = cv2.imread('data/Lena.png', cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('data/Lena_rotated.png', cv2.IMREAD_GRAYSCALE)

detector = cv2.ORB_vreate(100)
kps0, fea0 = detector.detectAndCompute(img0, None)
kps1, fea1 = detector.detectAndCompute(img1, None)