# 📹 AI-Powered Motion Detection Script (Starter)
# This uses your webcam (on PC) or test video (on Colab) to detect motion.

import cv2

# Start your webcam (0 = default camera)
cam = cv2.VideoCapture(0)

# Read the first two frames for comparison
ret, frame1 = cam.read()
ret, frame2 = cam.read()

while cam.isOpened():
    # Take the difference between current and previous frame
    diff = cv2.absdiff(frame1, frame2)

    # Convert the difference to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Smooth the image to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold the image to highlight changes
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Show the threshold output
    cv2.imshow("Motion Detection", thresh)

    # Update frames for next comparison
    frame1 = frame2
    ret, frame2 = cam.read()

    # Exit when 'q' is pressed
    if cv2.waitKey(10) == ord('q'):
        break

# Release everything when done
cam.release()
cv2.destroyAllWindows()
