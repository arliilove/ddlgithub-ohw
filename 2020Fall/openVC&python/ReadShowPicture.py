import numpy as np
import cv2

img = cv2.imread('d:\AFG1022.jpg',cv2.IMREAD_UNCHANGED)
img90 = np.rot90(img)
size = img90.shape
print(size)
img90S = cv2.resize(img90,(img90.shape[0],img90.shape[1]))
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img90S)
cv2.waitKey(0)
cv2.destroyAllWindows()