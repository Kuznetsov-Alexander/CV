import cv2

path = r'C:\Users\HONOR\Downloads\main\Learn\pet_projects\CV\CV\video\video.mp4'

def read_and_write_video():
    video = cv2.VideoCapture(path)

    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4
    video_writer = cv2.VideoWriter("output.mp4", fourcc, fps, (w, h))

    while True:
        ok, img = video.read()

        cv2.imshow('Video', img)
        video_writer.write(img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    video.release()
    video_writer.release()
    cv2.destroyAllWindows()
    print("Видео успешно сохранено как output.avi")

read_and_write_video()