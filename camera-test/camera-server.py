#!/usr/bin/env python3
from flask import Flask, Response
import cv2
import time
import threading

app = Flask(__name__)

# ==============================
# Camera Initialization
# ==============================
cap = cv2.VideoCapture("/dev/video1", cv2.CAP_V4L2)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 5)

if not cap.isOpened():
    raise RuntimeError("❌ Cannot open /dev/video1")

latest_frame = None
lock = threading.Lock()

# ==============================
# Frame Grabber Thread
# ==============================
def grab_frames():
    global latest_frame
    while True:
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.1)
            continue

        with lock:
            latest_frame = frame.copy()

        time.sleep(0.02)  # prevent CPU hog

threading.Thread(target=grab_frames, daemon=True).start()

# ==============================
# MJPEG Generator
# ==============================
def generate_mjpeg():
    while True:
        with lock:
            if latest_frame is None:
                continue
            frame = latest_frame.copy()

        ret, jpeg = cv2.imencode(".jpg", frame)
        if not ret:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n"
            b"Cache-Control: no-cache\r\n\r\n"
            + jpeg.tobytes() +
            b"\r\n"
        )

        time.sleep(0.2)  # 5 FPS output

# ==============================
# Web Routes
# ==============================
@app.route("/")
def index():
    return """
    <html>
      <head>
        <title>DQ1 Camera</title>
      </head>
      <body>
        <h1>/dev/video1 Live Stream</h1>
        <img src="/video_feed" />
      </body>
    </html>
    """

@app.route("/video_feed")
def video_feed():
    return Response(
        generate_mjpeg(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
    )

# ==============================
# Main
# ==============================
if __name__ == "__main__":
    print("✅ Starting Flask MJPEG server on 0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, threaded=True)
