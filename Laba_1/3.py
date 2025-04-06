import cv2

path = r'C:\Users\HONOR\Downloads\main\Учеба\pet_projects\CV\CV\video\video.mp4'
cap = cv2.VideoCapture(path)
if not cap.isOpened():
    print("Ошибка: не удалось открыть видеофайл")
    exit()

while True:
    ret, frame = cap.read()
    if not(ret):
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
