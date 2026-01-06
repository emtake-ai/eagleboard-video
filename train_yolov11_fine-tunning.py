from ultralytics import YOLO

DATASET = "dataset.yaml"
MODEL = "yolo11n.pt"

def main():
    model = YOLO(MODEL)

    model.train(
        task="detect",
        data=DATASET,
        epochs=80,
        imgsz=640,
        batch=32,
        device=0,
        workers=8,
        name="yolo11_ai-mf",
        close_mosaic=10,
        mosaic=0.8,
        autoanchor=True,
        optimizer="AdamW",
        lr0=0.001,
        cos_lr=True
    )

if __name__ == "__main__":
    main()
