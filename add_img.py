#! /usr/bimn/pyhon3

import numpy as np 
import cv2
print(cv2.__version__)
cat_img=cv2.imread('cat.jpeg')
dog_img=cv2.imread('dog.jpeg')
# adding tywo images
add_img=cv2.add(cat_img,dog_img)
#printing two images
#     frame name variable
cv2.imshow('dc',add_img)
cv2.waitKey(0)

