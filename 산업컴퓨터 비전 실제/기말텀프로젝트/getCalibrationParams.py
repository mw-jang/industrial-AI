import numpy as np
import cv2
import glob
import pickle


cv2.useOptimized()

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

BOARD_SIZE = (9,6)

objp = np.zeros((BOARD_SIZE[1]*BOARD_SIZE[0],3), np.float32)
objp[:,:2] = np.mgrid[0:BOARD_SIZE[0],0:BOARD_SIZE[1]].T.reshape(-1,2)

objpoints = []
imgpoints = []


images = glob.glob('data/chessboard.jpg')
counter = 0
cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)



for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, BOARD_SIZE ,None)

    if ret == True:
        counter += 1
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, BOARD_SIZE, corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(200)
        print (fname)

cv2.destroyAllWindows()
print('Number of photos processed: ', counter)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

cal = [mtx, dist, rvecs, tvecs]
points = [objpoints, imgpoints]
f = open('data/calibParams.pckl','wb')
pickle.dump(cal, f)
f.close()

f = open('data/points.pckl','wb')
pickle.dump(points, f)
f.close()
