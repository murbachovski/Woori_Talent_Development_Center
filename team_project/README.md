## 🎁파일 실행 방법
```
설명
```

## 🎁구현 이미지 및 영상
BodyPix is an open-source machine learning model which allows for person and
body-part segmentation. This has previously been released as a
[Tensorflow.Js](https://blog.tensorflow.org/2019/11/updated-bodypix-2.html)
project.

This repo contains a set of pre-trained BodyPix Models (with both MobileNet v1
and ResNet50 backbones) that are quantized and optimized for the Coral Edge
 TPU. Example code is provided to enable inferencing on generic platforms as
 well as an optimized version for the Coral Dev Board.

Body-Part Segmentation
:-------------------------:
![](media/segmentation.gif)

<p align="center">
  <img src="media/segmentation.gif" alt="Body-Part Segmentation">
</p>


*The above images show two possible applications of BodyPix. The left shows body-part
 segmentation (on an [example video](https://github.com/intel-iot-devkit/sample-videos/blob/master/head-pose-face-detection-female-and-male.mp4)) with bounding boxes and PoseNet-style skeletons. The right
 shows anonymous population flow. Both are running on the Coral Dev Board; see below for
 information on enabling these modes on the Dev Board or on a generic platform.*
