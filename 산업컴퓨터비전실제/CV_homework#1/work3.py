# 산업 컴퓨터 비전 실제 과제 3.주파수 도메인 필터링
# 2020254007 장민우

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('data/Lena.png',0).astype(np.float32) / 255

# 사용자로부터 반지름을 입력받아서 그 크기만큼의 원을 그린후
radius = np.int64(input("반지름을 입력:"))
red = (0, 0, 255)
center = image.shape[0]//2
radImg = cv2.circle(image, (center, center), radius, red, 5)

# DFT를 통해 주파수 도메인으로 변경후
fft = cv2.dft(radImg, flags=cv2.DFT_COMPLEX_OUTPUT)
shifted = np.fft.fftshift(fft, axes=[0,1])

magnitude = cv2.magnitude(shifted[:,:,0], shifted[:,:,1])
magnitude = np.log(magnitude)

#IDFT함
restored = cv2.idft((fft), flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

#Low pass or High Pass
freq = input("Low or High:")

#DFT 결과에 곱해줌
fft = fft*radius
sz = 25
mask = np.zeros(fft.shape, np.uint8)
mask[image.shape[0]//2-sz:image.shape[0]//2+sz,
    image.shape[1]//2-sz:image.shape[1]//2+sz,
    :] = 1

if freq == "H":
    shifted *= 1 - mask #high 프리퀀시
elif freq == "L":
    shifted *= mask   #low 프리퀀시

fft = np.fft.ifftshift(shifted, axes=[0,1])
filtered = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
mask_new = np.dstack((mask, np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)))

plt.subplot(131)
plt.axis('off')
plt.title('circle')
plt.imshow(radImg, cmap='gray')

plt.subplot(132)
plt.axis('off')
plt.title('frequancy')
plt.imshow(filtered, cmap='gray')

plt.tight_layout()
plt.show()


