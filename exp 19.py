import cv2
import numpy as np

img = cv2.imread('flower.jpg', 0)

if img is not None:
    kernel = np.ones((3, 3), np.uint8)

    erosion = cv2.erode(img, kernel, iterations=1)

    cv2.imshow('Original Image', img)
    cv2.imshow('Eroded Image', erosion)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
