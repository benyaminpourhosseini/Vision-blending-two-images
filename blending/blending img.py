import numpy as np
import cv2

I = cv2.imread('damavand.jpg',cv2.IMREAD_UNCHANGED)
#cv2.imshow('damavand',I)


J = cv2.imread('eram.jpg')
#cv2.imshow('eram',J)

print(I.shape)
print(J.shape)

k1 = I.copy()
k1[::2,::2,:] = J[::2,::2,:]

k2 = I//2+J//2

k3 =  (0.5*I + 0.5*J).astype(np.uint8)

k4 =  cv2.addWeighted(I, 0.2, J, 0.8, 0)  #other shape of method3

cv2.imshow('method1',k1)
cv2.imshow('method2',k2)
cv2.imshow('method3',k3)
cv2.imshow('method4',k4)

#cv2.imshow('damavand',I)
#cv2.imshow('eram',J)

cv2.imwrite('blending method1.jpg',k1)
cv2.imwrite('blending method2.jpg',k2)
cv2.imwrite('blending method3.jpg',k3)
cv2.imwrite('blending method4.jpg',k4)

cv2.waitKey()
cv2.destroyAllWindows()

