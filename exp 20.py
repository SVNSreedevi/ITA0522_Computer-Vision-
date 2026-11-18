import cv2
import numpy as np

img = cv2.imread('flower.jpg', 0)

if img is not None:
    kernel = np.ones((3, 3), np.uint8)

    dilation = cv2.dilate(img, kernel, iterations=1)

    cv2.imshow('Original Image', img)
    cv2.imshow('Dilated Image', dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
