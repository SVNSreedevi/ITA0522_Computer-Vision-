import cv2
import numpy as np

img = cv2.imread("flower.jpg")

if img is None:
    print("Image not found!")
else:
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    result = np.hstack((img, blur))

    cv2.imshow("Original and Blurred Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
