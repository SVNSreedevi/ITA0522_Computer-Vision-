import cv2
import numpy as np

# Read the image
img = cv2.imread("flower.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Convert grayscale images to color format
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    equalized = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

    # Display images side by side
    result = np.hstack((gray, equalized))

    cv2.imshow("Original and Equalized Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
