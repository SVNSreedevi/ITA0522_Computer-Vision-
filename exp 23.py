import cv2
import numpy as np

img = cv2.imread('flower.jpg')

if img is not None:
    kernel = np.ones((3, 3), np.uint8)

    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

    cv2.imshow('Original Image', img)
    cv2.imshow('Top Hat Image', tophat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
