import cv2

path = r'C:\Users\HONOR\Downloads\main\Learn\pet_projects\CV\CV\images\photo.jpg'

# загрузка и обработка изображения
img_bgr = cv2.imread(path)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

# создаем окна для отображения изображения с фиксированным размером
cv2.namedWindow('Original (BGR)', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original (BGR)', 600, 400)

cv2.namedWindow('HSV Format', cv2.WINDOW_NORMAL)
cv2.resizeWindow('HSV Format', 600, 400)


cv2.imshow('BGR', img_bgr)
cv2.imshow('HSV', img_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()