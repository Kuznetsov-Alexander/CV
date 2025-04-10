import cv2


#Подключаем камеру
cap = cv2.VideoCapture(0)

# Параметры креста
cross_size = 80      # Длина лучей
thickness = 20       # Толщина прямоугольников
color = (0, 0, 255)  # Красный цвет
line_thickness = 2    # Толщина линий

while True:
    ret, frame = cap.read()

    height, width = frame.shape[:2] #срез массива для цветного изображения у которого первые два элемента это высота и ширина
    center_x, center_y = width // 2, height // 2

# cv2.rectangle(img, pt1, pt2, color, thickness) img - изображение, на котором рисуем / pt1 - координаты левого верхнего угла (x1, y1)
# pt2 - координаты правого нижнего угла (x2, y2) / color - цвет в формате BGR (синий, зелёный, красный) / thickness - толщина линии (-1 для заливки)

    # Вертикальный прямоугольник (с вырезом в центре)
    cv2.rectangle(frame, (center_x - thickness // 2, center_y - cross_size), (center_x + thickness // 2, center_y - thickness // 2), color, line_thickness)
    cv2.rectangle(frame, (center_x - thickness // 2, center_y + thickness // 2), (center_x + thickness // 2, center_y + cross_size), color, line_thickness)

    # Горизонтальный прямоугольник (полностью)
    cv2.rectangle(frame, (center_x - cross_size, center_y - thickness // 2), (center_x + cross_size, center_y + thickness // 2), color, line_thickness)

    cv2.imshow('Cross', frame)


    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()