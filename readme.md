## Video using still images


#### check on how to do classification

##### git clone huggingface
```text
git clone https://huggingface.co/datasets/emtake-ai/classification
cd ./classification
```


##### dataset download  
[huggingface dataset download](https://huggingface.co/datasets/emtake-ai/classification)  

```text
download "dataset_classification_mobilenet.zip" from huggingface "in files and versions" inside current directory which is ./classifcation after git clone classification
```

##### train classification using mobilenet
```text
python3 ./train_classification_mobilenet.py
```
##### after completing the training, you can get the training result "mobilenet_classification.h5"

##### predict the result of training
```text
python3 ./predict_classificatoin.py
in here you should change model name from written to "mobilenet_classification.5"
```


## Video using Camera

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

#### check fine-tunning from ultralytics

##### you make dataset.yaml as below.

```text
path: /home/user/dataset
train: images/train
val: images/val
test: images/test

names:
  0: person
  1: dog
  2: cat
```


##### git clone huggingface
```text
git clone https://huggingface.co/datasets/emtake-ai/detection
cd ./detection
```

##### dataset download  
[huggingface dataset download](https://huggingface.co/datasets/emtake-ai/detection)  

```text
download "dataset_detection.zip" from huggingface "in files and versions" inside current directory which is ./detection after git clone detection
```

##### you should annotate the image after checking below link  
[how to annotate using lableImg](https://www.youtube.com/watch?v=nV26hK3CxNM)

##### you can train with fine-tunning after annotation using labelImg
```text
python3 ./train_yolov11_fine-tunning.py
```

##### after it, you can get "runs/detect/yolo11_ai-mf/weights/best.pt", the training result.
```text
python3 ./yolov11-tinetunning.py
```


