import cv2
import urllib.request
import numpy as np

# URL камеры телефона
url = "http://172.20.10.6:8080/shot.jpg"

while True:
    # Получаем изображение с телефона
    img_resp = urllib.request.urlopen(url) # Отправляет HTTP-запрос к серверу IP Webcam на телефоне и получает ответ.
    img_arr = np.array(bytearray(img_resp.read()), dtype=np.uint8) #Преобразует полученные бинарные данные в numpy-массив.
    frame = cv2.imdecode(img_arr, -1) #Декодирует массив байтов в изображение OpenCV.

    # Отображаем видео
    cv2.imshow('Camera', frame)

    # Выход по ESC
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()