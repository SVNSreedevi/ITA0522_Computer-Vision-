import cv2
import os

video_path = r"C:\Users\HP\OneDrive\Desktop\computer vision\lab\video.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video. Check the video path.")
    exit()

print("Press q to stop the video")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Normal Video", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
