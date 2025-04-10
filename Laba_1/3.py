import cv2

path = r'C:\Users\HONOR\Downloads\main\Learn\pet_projects\CV\CV\video\video.mp4'
cap = cv2.VideoCapture(path)
if not cap.isOpened():
    print("Ошибка: не удалось открыть видеофайл")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # ширина окна
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #высота окна
fps = cap.get(cv2.CAP_PROP_FPS) #фпс
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))



while True:
    ret, frame = cap.read()
    if not(ret):
        break
    resized_frame = cv2.resize(frame, (width // 2, height // 10)) # изменяем размер окна
    cv2.imshow('frame', resized_frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
