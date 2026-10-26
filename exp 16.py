import cv2

img = cv2.imread('flower.jpg', 0)

if img is not None:
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    cv2.imshow('Original Image', img)
    cv2.imshow('Sobel X', cv2.convertScaleAbs(sobelx))
    cv2.imshow('Sobel Y', cv2.convertScaleAbs(sobely))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
