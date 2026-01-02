
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