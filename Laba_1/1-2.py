import cv2

import os
print("Файлы в текущей папке:", os.listdir('.'))
img = cv2.imread('')
cv2.imshow('output', img)
cv2.waitKey(0)