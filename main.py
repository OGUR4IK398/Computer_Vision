import cv2
import numpy as np
import time

# image = cv2.imread("./kinopoisk.ru-Shrek-13985.jpg")

# Изменить цвет и способ кодировки
# img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Работа с конкретными пикселями картинки
# [x, y]
# image[10:50, 10:50] = [255, 255, 255]

# BGR = RGB [x, y, n], n - от 0 до 2 - BGR ставим яркость для одного из цветов
# image[:, :, 1] = 0

# для всех пикселей всех значенй цветов
# image[:, :, :] += 250

# Поменять типы данных внутри
img = image.astype(np.float64)
img[:, :, :] += 50
img = np.clip(img, 0, 255)
img = img.astype(np.uint8)

# Вывод изображения
cv2.imshow('shrek', img)

# Ожидает нажатия любой кнопки с клавиатуры
cv2.waitKey(0)

print(image)
# time.sleep(5)
