#! /usr/bin/python3

import cv2 
color_img=cv2.imread('cat.jpeg',cv2.IMREAD_COLOR)
gray_img=cv2.imread('cat.jpeg',cv2.IMREAD_GRAYSCALE)
unch_img=cv2.imread('cat.jpeg',cv2.IMREAD_UNCHANGED)
#printing the images

cv2.imshow('color',color_img)
cv2.imshow('gray',gray_img)
cv2.imshow('unchanged',unch_img)

# to hold the pop up

cv2.waitKey(0)




