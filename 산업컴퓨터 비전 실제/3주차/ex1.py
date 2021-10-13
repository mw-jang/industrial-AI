import argparse
import cv2
import numpy as np
import random

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='data/Lena.png', help='Image path.')
parser.add_argument('--out_png', default="lena_comp.png", help='Output image')
params = parser.parse_args()
image = cv2.imread(params.path)
image_to_show = np.copy(image)
w, h = image.shape[1], image.shape[0]

mouse_pressed = False
s_x = s_y = e_x = e_y = 50

def mouse_callback(event, x, y, flags, parm):
    global image_to_show, s_x, s_y, e_x, e_y, mouse_pressed
    if event == cv2.EVENT_MOUSEMOVE:
        s_x = x
        s_y = y

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

def rand_pt() :
    return (random.randrange(w), random.randrange(h))

finish = False
while not finish:
    cv2.imshow("image", image_to_show)
    key = cv2.waitKey(0)

    if key == ord('r'):
        cv2.rectangle(image_to_show, (s_x,s_y), rand_pt(), (0, 255, 0), 3)
    elif key == ord('l'):
        cv2.line(image_to_show, (s_x,s_y), rand_pt(), (0, 255, 0), 3)
    elif key == ord('a'):
        cv2.arrowedLine(image_to_show, (s_x,s_y), rand_pt(), (0, 255, 0), 3)
    elif key == ord('w'):
        cv2.imwrite(params.out_png, image_to_show, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    elif key == ord('c'):
        image_to_show = np.copy(image)
    elif key == 27:
        finish = True

