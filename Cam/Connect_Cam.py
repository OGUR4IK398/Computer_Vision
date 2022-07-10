import cv2

cam = cv2.VideoCapture(0) # Можно файл по адресу



while True:
    ret, frame = cam.read()  # Возвращает 2 значение (bool, frame)
    if ret:
        cv2.imshow("OUTPUT", frame)
    else:
        break

    # При нажатии на q выходим из цикла
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
