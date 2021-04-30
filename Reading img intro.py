from matplotlib import pyplot as plt
import numpy as np
import cv2 

img1= cv2.imread("/home/benyamin/Desktop/Computer-Vision/Lab/cv-lab1/masoleh_gray.jpg",cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('/home/benyamin/Desktop/Computer-Vision/Lab/cv-lab2/masoleh.jpg',cv2.IMREAD_UNCHANGED)
img3 = cv2.imread('/home/benyamin/Desktop/Computer-Vision/Lab/cv-lab2/masoleh.jpg')

print(img1.shape)
print(img2.shape)

#cv2.imshow('Masoleh Village Gray' , img1)
#cv2.imshow('Masoleh Village RGB' , img2)

print(img1[10,20])
print(img2[10,20])
print(img3[10,20])


#cv2.waitKey(10000)     #display the image for 10 seconds
#cv2.destroyAllWindows()

#plt.imshow(img3)
#plt.show()

#Are the image colors strange? Remember scipy/matplotlib use the RGB
#system, while opencv uses the BGR system. Reading an image with opencv
#and displaying with matplotlib makes the blue and red channels swapped.
#plt.imshow(img3[:,:,::-1])
#plt.show()

#img3[:,:,1] = 0 #set green channel equal zero
#plt.imshow(img3[:,:,::-1])
#plt.show()

#cv2.imwrite('masoleh_zero green channel.jpg',img3)

B = img3[:,:,0]
G = img3[:,:,1]
R = img3[:,:,2]

cv2.imshow('just blue ',B)	#gray image
cv2.imshow('just green',G)	#gray image
cv2.imshow('just red',R)	#gray image
cv2.imshow('original',img3)
cv2.waitKey()
