import cv2
import numpy as np

# Read the image
img = cv2.imread("flower.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    outline = cv2.Canny(gray, 100, 200)

    # Convert outline to color format
    outline = cv2.cvtColor(outline, cv2.COLOR_GRAY2BGR)

    # Display original and outline side by side
    result = np.hstack((img, outline))

    cv2.imshow("Original and Outline Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
