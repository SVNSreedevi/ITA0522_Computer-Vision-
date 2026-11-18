import cv2

img = cv2.imread('flower.jpg')

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    cv2.imshow('Original Image', img)
    print("Image loaded successfully!")
    print("Object recognition is performed.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
