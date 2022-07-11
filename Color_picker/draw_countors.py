import cv2


def get_contours(img, mask):
    contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # Получаем именно контуры
    contours = contours[1]
    cv2.drawContours(img, contours, -1, (255, 0, 255), 3)
    return img
