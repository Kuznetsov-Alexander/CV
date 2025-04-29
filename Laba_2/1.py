import cv2
import numpy as np


cap = cv2.VideoCapture(0)

# Диапазоны красного цвета в HSV
l_red1 = np.array([0, 120, 70])
up_red1 = np.array([10, 255, 255])
l_red2 = np.array([160, 120, 70])
up_red2 = np.array([180, 255, 255])

# Ядро для морфологических операций
kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Конвертация в HSV (Задание 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Создание маски для красного
    mask1 = cv2.inRange(hsv, l_red1, up_red1)
    mask2 = cv2.inRange(hsv, l_red2, up_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Морфологические операции (Задание 3)
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2) # открытие Эрозия + дилатация. Удаление мелких белых точек (шумов) Сохранение формы основного объекта

    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel, iterations=2) # Закрытие Дилатация + эрозия. Заполнение мелких чёрных дыр внутри объекта Сглаживание границ
# iterations=2 применяется для получения баланса между очисткой и сохранением формы объекта.


    # Поиск контуров (Задания 4-5)
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #contours — список найденных контуров. _ — игнорирование иерархии (не нужна для простого трекинга).
    #RETR_EXTERNAL — возвращает только внешние контуры.
    # Метод упрощения контура: CHAIN_APPROX_SIMPLE — сжимает контур, оставляя только ключевые точки (для прямоугольника вернёт 4 угла вместо всех точек сторон).
    if contours:
        # Выбор контура с максимальной площадью
        max_contour = max(contours, key=cv2.contourArea) # Из списка всех контуров (contours) выбирает контур с максимальной площадью. key=cv2.contourArea указывает, что сравнение контуров происходит по их площади.
        area = cv2.contourArea(max_contour) #Вычисляет площадь выбранного контура в пикселях.

        # Фильтр по площади
        if area > 500:
            # Построение прямоугольника
            x, y, w, h = cv2.boundingRect(max_contour) # Возвращает координаты прямоугольника, описывающего контур: (x, y) — левый верхний угол. (w, h) — ширина и высота.
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2) # Рисует прямоугольник на изображении frame.

            # Дополнительно: расчет центра через моменты
            M = cv2.moments(max_contour) # вычисляет моменты изображения для заданного контура. Моменты — это статистические характеристики формы объекта, позволяющие вычислить его свойства (площадь, центр, ориентацию и др.).
            cx = int(M['m10'] / M['m00']) # M['m00'] — площадь контура (аналогично cv2.contourArea).
            cy = int(M['m01'] / M['m00']) # M['m10'], M['m01'] — моменты первого порядка, используемые для расчёта центра.
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)


    cv2.imshow('', cleaned)
    cv2.imshow('Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()