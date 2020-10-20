import numpy as np
import cv2
global n
zong = 0
n = 0
img1 = cv2.imread('1.png',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('2.png',cv2.IMREAD_GRAYSCALE)
height, width = img1.shape
for line in range(height):
    for pixel in range(width):
        if img1[line][pixel] != img2[line][pixel]:
            n = n + 1
print(n)