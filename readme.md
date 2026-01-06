
#### Check if the camera device exists

```text
ls -l /dev/video*
```

#### Verify that the driver detects the camera

```text
v4l2-ctl --list-devices
```

#### List supported formats / resolutions / FPS

```text
v4l2-ctl -d /dev/video0 --list-formats-ext
```

#### check camera test

```text
python3 ./camera.py
```

you can see the live streaming from camera if run above code.

#### check yolov11 from ultralytics
```text
python3 ./yolov11.py
```

you can see the live streaming with object detection if run above code.

#### check fine tunning from ultralytics
```text
dataset.yaml
path: /home/user/dataset
train: images/train
val: images/val
test: images/test

names:
  0: person
  1: dog
  2: cat
```



