import os, cv2, random, time
import numpy as np
import tensorflow as tf

DATASET_DIR = ".../dataset/train"
MODEL_PATH  = "classification.keras"
IMG_SIZE = 224
CLASS_NAMES = ["person", "dog", "cat"]

# -------------------------------
# Load model
# -------------------------------
model = tf.keras.models.load_model(MODEL_PATH)

# -------------------------------
# Load dataset file list
# -------------------------------
file_map = {}
for cls in CLASS_NAMES:
    cls_dir = os.path.join(DATASET_DIR, cls)
    file_map[cls] = [os.path.join(cls_dir, f) for f in os.listdir(cls_dir)
                     if f.lower().endswith((".jpg", ".png", ".jpeg"))]

# -------------------------------
# Main loop
# -------------------------------
while True:
    gt = random.choice(CLASS_NAMES)
    img_path = random.choice(file_map[gt])

    frame = cv2.imread(img_path)
    if frame is None:
        continue

    img = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)[0]
    cls_id = np.argmax(pred)
    conf = pred[cls_id]

    label = f"GT: {gt} | Pred: {CLASS_NAMES[cls_id]} ({conf:.2f})"

    show = cv2.resize(frame, (640,480))
    cv2.putText(show, label, (10,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0,255,0), 2)

    cv2.imshow("MobileNet Dataset Test", show)
    if cv2.waitKey(1) == 27:
        break

    time.sleep(1)   # 🔥 1초 유지

cv2.destroyAllWindows()
