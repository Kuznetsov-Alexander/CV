import cv2

img = cv2.imread('images/photo.jpg')
cv2.imshow('output', img)
cv2.waitKey(0)