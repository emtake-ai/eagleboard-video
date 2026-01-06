import cv2
from ultralytics import YOLO

WEIGHT = "yolo11n.pt"
model = YOLO(WEIGHT)

cap = cv2.VideoCapture("/dev/video0")

while True:
    ret, frame = cap.read()
    results = model(frame, imgsz=640, conf=0.4, verbose=False)

    annotated = results[0].plot()
    cv2.imshow('d', annotated)

    if cv2.waitKey(1) == 27:
        break

    