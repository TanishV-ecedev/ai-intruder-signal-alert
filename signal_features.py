# 📊 signal_features.py
# Track motion intensity and plot it as a signal graph

import cv2
import numpy as np
import matplotlib.pyplot as plt

motion_signal = []

# Load video
video = cv2.VideoCapture(cv2.samples.findFileOrKeep("vtest.avi"))

while True:
    ret, frame1 = video.read()
    ret, frame2 = video.read()
    if not ret:
        break

    # Frame difference
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Calculate motion intensity (how much white = how much movement)
    motion_value = np.sum(thresh) / 255
    motion_signal.append(motion_value)

video.release()

# Plot the motion signal
plt.figure(figsize=(10, 4))
plt.plot(motion_signal, color='blue')
plt.title("📈 Motion Signal Over Time")
plt.xlabel("Frame")
plt.ylabel("Motion Intensity")
plt.grid(True)
plt.tight_layout()
plt.show()
