import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((480, 640), np.uint8)
cv2.ellipse(image, (32, 240), (200, 100), 0, 0, 360, 255, -1)

m = cv2.moments(image)
for name, val in m.items():
    print(name, '\t', val)

print('Center X estimated:', m['m10'] / m['m00'])
print('Center Y estimated:', m['m01'] / m['m00'])
