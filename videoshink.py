import cv2

# Укажите путь к видеофайлу
video_path = "surprise.mp4"

# Открываем видеофайл
cap = cv2.VideoCapture(video_path)

# Проверяем, удалось ли открыть файл
if not cap.isOpened():
    print("Ошибка: Не удалось открыть видеофайл")
    exit()

# Читаем и отображаем кадры в цикле
while True:
    ret, frame = cap.read()

    # Если видео закончилось, выходим из цикла
    if not ret:
        break

    # Отображаем кадр
    cv2.imshow("Video", frame)

    # Ждем 25 мс и проверяем нажатие клавиши 'q' для выхода
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
