import cv2

cap = cv2.VideoCapture(0)

# Параметры креста
cross_size = 60
thickness = 20

# Получаем первый кадр
ret, first_frame = cap.read()

height, width = first_frame.shape[:2]
center_x, center_y = width // 2, height // 2

# Получаем цвет центрального пикселя BGR
b, g, r = first_frame[center_y, center_x]

if r > g and r > b:
    color = (0, 0, 255)
    color_name = "КРАСНЫЙ"
elif g > b:
    color = (0, 255, 0)
    color_name = "ЗЕЛЕНЫЙ"
else:
    color = (255, 0, 0)
    color_name = "СИНИЙ"

print(f"Центральный пиксель: B={b}, G={g}, R={r}")
print(f"Доминирующий канал: {color_name}")

while True:
    ret, frame = cap.read()
    # Рисуем крест
    # Горизонтальная часть
    cv2.rectangle(frame, (center_x - cross_size, center_y - thickness//2), (center_x + cross_size, center_y + thickness//2), color, -1)
    # Вертикальная часть
    cv2.rectangle(frame, (center_x - thickness//2, center_y - cross_size), (center_x + thickness//2, center_y + cross_size), color, -1)

    cv2.imshow('Color Cross', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()