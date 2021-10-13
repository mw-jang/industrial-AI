import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/Lena.png',0)
t, t_otsu = cv2.threshold(img, -1, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


while True:
    print("Pressed[1] : Erosion")
    print("Pressed[2] : Dilation")
    print("Pressed[3] : Opening")
    print("Pressed[4] : Closing")
    pressed = np.int64(input("1~4중 선택하시오 : "))
    if pressed < 5:
        break
    else:
        print("1~4까지 입력하시오.")
while True:
    number = np.int64(input("iterations number : "))
    if number > 0:
        break


eroded = cv2.morphologyEx(t_otsu, cv2.MORPH_ERODE, (3, 3), iterations=number)
dilated = cv2.morphologyEx(t_otsu, cv2.MORPH_DILATE, (3, 3), iterations=number)

opened = cv2.morphologyEx(t_otsu, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=number)
closed = cv2.morphologyEx(t_otsu, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=number)

plt.figure(figsize=(10,10))
plt.subplot(231)
plt.axis('off')
plt.title('binary')
plt.imshow(t_otsu, cmap='gray')

if pressed == 1:
    plt.subplot(232)
    plt.axis('off')
    plt.title('erode %d times' % number)
    plt.imshow(eroded, cmap='gray')

elif pressed == 2:
    plt.subplot(232)
    plt.axis('off')
    plt.title('dilate %d times' % number)
    plt.imshow(dilated, cmap='gray')

elif pressed == 3:
    plt.subplot(232)
    plt.axis('off')
    plt.title('open %d times' % number)
    plt.imshow(opened, cmap='gray')

elif pressed == 4:
    plt.subplot(232)
    plt.axis('off')
    plt.title('close %d times' % number)
    plt.imshow(closed, cmap='gray')

plt.tight_layout()
plt.show()
