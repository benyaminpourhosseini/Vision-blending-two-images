import numpy as np
import cv2
img = cv2.imread('eram.jpg',cv2.IMREAD_UNCHANGED)
cv2.imshow('original', img)

for i in range(3):
    test = np.zeros(img.shape, dtype = np.uint8)
    test[:,:,i] = img[:,:,i]
    cv2.imshow('channel %s'%i,test)
    cv2.imwrite('channel %s.jpg'%i,test)
    cv2.waitKey()
