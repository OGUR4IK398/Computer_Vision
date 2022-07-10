import cv2

rgb = cv2.imread()
rgb = cv2.resize(rgb, (700, 350))

cv2.imshow('rgb', rgb)

# [x, y, [b, g, r]] - структура пикселя изображения


i = 1
while True:

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()