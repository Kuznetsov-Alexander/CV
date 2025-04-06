import cv2

path = 'images/photo.jpg'
img = cv2.imread(path, cv2.IMREAD_COLOR) # загрузка в цветном режиме BGR

cv2.imshow('Мое окно', img)
cv2.waitKey(0)

cv2.destroyAllWindows()