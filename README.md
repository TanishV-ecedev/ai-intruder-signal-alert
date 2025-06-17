# 🔒 AI-Powered Intruder Detection & Signal-Aware Alert System

A beginner-friendly open-source project using Python and OpenCV to detect motion or intruders from a camera feed.  
Built by Tanish to learn computer vision, signal tracking, and eventually AI + embedded alert systems.

---

## 🎯 Objective

Detect movement from a camera feed, capture frames of activity, and later build smart features like signal-based motion patterns, AI classification, and real-time alerts.

---

## 🚀 What’s Working Now (June 2025)

- [x] Motion detection using OpenCV (frame difference)
- [x] Basic motion graph (signal-style tracking)
- [x] Frame saving (image snapshots)
- [x] Telegram alert integration (live bot, sends alerts)
- [ ] ML model to classify patterns (planned)

> 📲 Bot: [@tanish_intruder_bot](https://t.me/tanish_intruder_bot)

---

## 🛠 Tech Stack

- Python
- OpenCV
- NumPy
- Google Colab (for now)
- GitHub

---

## 📂 Project Structure.

```
ai-intruder-signal-alert/
├── src/
│   ├── detect.py             ← Main motion detection script
│   ├── signal_features.py    ← (Later) Converts motion into graph-style signal
│   ├── alert.py              ← (Later) Sends alert via Telegram or Email
├── images/                   ← Intruder snapshots
├── README.md
├── requirements.txt
```
---

## 📅 Future Milestones

- Add signal tracking graph (like motion over time)
- Add ML model to classify "idle" vs "intruder"
- Add alert system (Telegram bot or email)
- Optional: run on Jetson Nano or ESP32-CAM later

---

## 👨‍💻 Built By

**Tanish Vangapandu**  
Aspiring Embedded & AI Developer | ECE @ SRM AP  
Learning by building open-source projects from scratch 🚀
