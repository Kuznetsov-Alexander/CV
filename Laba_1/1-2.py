import cv2

path = 'images/photo.jpg'
img = cv2.imread(path, cv2.IMREAD_UNCHANGED) # загружает изображение со всеми исходными данными включая прозрачность

cv2.imshow('Мое окно', img)
cv2.waitKey(0)

cv2.destroyAllWindows()