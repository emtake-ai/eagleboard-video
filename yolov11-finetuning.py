import cv2, time
from ultralytics import YOLO

MODEL = "runs/detect/yolo11_ai-mf/weights/best.pt"
CAM = "/dev/video0"

model = YOLO(MODEL)
names = model.names

cap = cv2.VideoCapture(CAM, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
    ret, frame = cap.read()
    if not ret:
        time.sleep(0.01)
        continue

    results = model(frame, imgsz=640, conf=0.4, verbose=False)[0]

    if results.boxes is not None:
        boxes = results.boxes.xyxy.cpu().numpy()
        classes = results.boxes.cls.cpu().numpy()
        confs = results.boxes.conf.cpu().numpy()

        for (x1, y1, x2, y2), cls, conf in zip(boxes, classes, confs):
            cls = int(cls)
            label = f"{names[cls]} {conf:.2f}"

            cv2.rectangle(frame,
                          (int(x1), int(y1)),
                          (int(x2), int(y2)),
                          (0,255,0), 2)

            cv2.putText(frame, label,
                        (int(x1), int(y1)-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0,255,0), 2)

    cv2.imshow("YOLOv11 putText", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
