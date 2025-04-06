import cv2

path = 'images/photo.jpg'
img = cv2.imread(path)

cv2.namedWindow('Мое окно', cv2.WINDOW_AUTOSIZE) #автоматически подгоняет размер окна под изображение


cv2.imshow('Мое окно', img)
cv2.waitKey(0)

cv2.destroyAllWindows()