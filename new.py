#!/usr/bin/python3
import cv2

print (cv2.__version__)
img_data=cv2.imread('maduri.jpeg')
print(img_data)
print (type (img_data))
print (img_data.shape)
cv2.imwrite('newmad.jpeg',img_data-50)
cv2.imshow('ds',img_data-50)
cv2.waitKey(0)
cv2.destroyAllWindows()
