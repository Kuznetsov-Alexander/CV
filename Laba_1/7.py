import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('7.avi', fourcc, fps, (width, height))

print(f"Начата запись видео {width}x{height} {fps:.1f} FPS") # округление до 1 знака после запятой

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('Recording', frame)


    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Запись сохранена как 7.avi")
# видео можно просмотреть по заданию 3