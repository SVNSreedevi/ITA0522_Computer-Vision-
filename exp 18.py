import cv2

img = cv2.imread('flower.jpg')

if img is not None:
    h, w = img.shape[:2]

    roi = img[10:108, 10:160]
    copied = roi.copy()

    rh, rw = copied.shape[:2]

    x = w - rw
    y = h - rh

    img[y:y+rh, x:x+rw] = copied

    cv2.imshow('Original Image', cv2.imread('flower.jpg'))
    cv2.imshow('Cropped ROI', roi)
    cv2.imshow('Copied and Pasted Image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
