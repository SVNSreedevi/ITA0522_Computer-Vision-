import cv2
import numpy as np

# Read the image
img = cv2.imread("flower.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert grayscale to color format for joining
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Join both images side by side
    result = np.hstack((img, gray))

    # Display both images in one window
    cv2.imshow("Original and Grayscale Images", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
