import cv2
import numpy as np
import functions as f
import time
# import draw_countors as dc

cam = cv2.VideoCapture(0)

# Получение заранее подобранных thresholds
thresholds = f.get_thresholds()


while True:
    ret, frame = cam.read()

    # Переворот и размытие изображения
    frame = frame[:, ::-1]

    frame_copy = frame.copy()

    frame = cv2.blur(frame, (20, 20))


    # Перевод в HSV, наложение маски thresholds
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, (np.array(thresholds[:3])), (np.array(thresholds[3:])))

    # Работа с изображение (убирание ряби)
    cv2.erode(mask, (3, 3),  iterations=2)
    cv2.dilate(mask, (3, 3), iterations=4)
    cv2.imshow('mask', mask)
    
    # _ обязательно, иначе беда
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(frame, contours, (-1), (255, 0, 255), 3)
    # cv2.imshow('frame', frame)

    # Выводим фигуру с наибольшим контуром
    if contours:
        big_contour = list(sorted(contours, key=cv2.contourArea, reverse=True))[0]
        cv2.drawContours(frame, big_contour, (-1), (255, 0, 255), 3)

        # Рисуем найденный объект в отдельном окне
        (x, y, w, h) = cv2.boundingRect(big_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Вырезаем часть со знаком:
        ro_img = frame_copy[y:y + h, x:x + w]
        cv2.imshow('sign', ro_img)

    cv2.imshow('frame', frame)

    # Обработка сохранения изображения по кнопке:
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite(f'images/{time.time()}.jpg', ro_img)

    # Quit by q-key
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
