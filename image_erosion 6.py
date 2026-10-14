import cv2
import numpy as np

# Read the image
img = cv2.imread("flower.jpg")

if img is None:
    print("Image not found!")
else:
    # Create kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(img, kernel, iterations=1)

    # Display both images side by side
    result = np.hstack((img, eroded))

    cv2.imshow("Original and Eroded Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
