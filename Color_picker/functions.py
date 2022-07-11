import cv2
import numpy as np


def get_thresholds():
    file = open('thresholds.txt', 'r')
    thresholds = list(map(int, file.read().split()))
    print(thresholds)
    file.close()
    return thresholds