import cv2
import os
from datetime import datetime

# Create 'images' folder if not there
if not os.path.exists("images"):
    os.mkdir("images")

cam = cv2.VideoCapture(0)  # 0 = default webcam

ret, frame1 = cam.read()
ret, frame2 = cam.read()

while cam.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Count white pixels = motion strength
    white_pixels = cv2.countNonZero(thresh)

    # Save image if movement is big enough
    if white_pixels > 5000:  # tweak this if needed
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"images/intruder_{timestamp}.jpg"
        cv2.imwrite(filename, frame1)
        print(f"[ALERT] Intruder snapshot saved: {filename}")

    cv2.imshow("Motion", thresh)
    frame1 = frame2
    ret, frame2 = cam.read()

    if cv2.waitKey(10) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
