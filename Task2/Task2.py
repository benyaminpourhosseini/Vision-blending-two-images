from matplotlib import pyplot as plt
import numpy as np
import cv2


I =cv2.imread('damavand.jpg')
J =cv2.imread('eram.jpg')

#k = cv2.addWeighted(I, 0.5, J, 0.5, 0)
#cv2.imshow('blending',k)
#cv2.waitKey()
step = np.arange(0,1,0.01)
for i in step:
    k = cv2.addWeighted(I, i, J, 1-i, 0)
    cv2.imshow('blending',k)
    cv2.waitKey(50)
cv2.destroyAllWindows()
