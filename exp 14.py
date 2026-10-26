import cv2
import numpy as np

img = cv2.imread('flower.jpg')

if img is not None:
    rows, cols = img.shape[:2]

    pts1 = np.float32([[50, 50], [200, 50],
                       [50, 200], [200, 200]])

    pts2 = np.float32([[10, 100], [200, 50],
                       [100, 250], [250, 250]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (cols, rows))

    cv2.imshow('Original Image', img)
    cv2.imshow('Perspective Transformation', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")

