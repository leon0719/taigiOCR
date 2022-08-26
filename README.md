English | [Chinese](README_ch.md)

# Applications

Recognize and save Chinese, mixed Hanji, Tâi-lô and Peh-oe-ji characters as text files

![image](images/result_ch.jpg "中")

![image](images/result_en.jpg "英")

![image](images/result_HAN_LO.jpg "漢羅")

![image](images/result_POJ.jpg "白話字")

# Installing

you can clone this git repo and install Docker images

```
git clone https://github.com/leon0719/taigiOCR.git
```

Using Docker image to build environment, install library, CUDA and CUDA Toolkit

```
#Create a folder to save pictures
mkdir img_data

docker run --gpus all -it --name OCR_ENV -v /path/to/taigiOCR:/workspace/ -v /path/to/img_data:/train_data/ --shm-size=120g --ulimit memlock=-1 leonhilty/ocr_search:v1.0.6 /bin/bash

```

Confirm that you are in the Docker environment

![image](/images/Docker_env.jpg "Docker環境")

## Generating DATASET

Using tools/train_test_split.py to generate Chinese, English, Japanese, POJ, mixed Hanji and Tâi-lô characters and to cut the training set(90%) and validation set(10%).
and simulated test data

```
cd tools/
python train_test_split.py
```

Generating Results

![image](images/ch.png "中")
![image](images/en.jpg "英")
![image](images/jp.jpg "日")
![image](images/POJ.jpg "白話字")
![image](images/TAI_LO.jpg "台羅")
![image](images/HAN_LO.jpg "漢羅")

Training Set and Validation Set

|          | Training Set       | Validation Set      |
| -------- | ------------ | ----------- |
| Chinese       | 360,000      | 40,000      |
| English |       | 360,000      | 40,000      |
| Japanese       | 360,000      | 40,000      |
| POJ   | 360,000      | 40,000      |
| Tâi-lô     | 360,000      | 40,000      |
| mixed Hanji     | 360,000      | 40,000      |
| Total(Images) | 2,160,000    | 240,000     |
| Number of characters   | 100,000,000+ | 17,000,000+ |

Folder Trees

```
/train_data/
    (Simulation test data)
    ├── test_ch
    ├── test_en
    ├── test_HAN_LO
    ├── test_jp
    ├── test_POJ
    ├── test_TAI_LO
    └── train_data
        ├── test (Validation set Img)
        ├── test_label.txt (Validation set Labels)
        ├── train (Training Set Img)
        └── train_label.txt (Training Set Labels)
```

## Training

Modify the PaddleOCR/configs/rec/PP-OCRv3/PP-OCRv3_rec.yml configuration file

|                         | Modify                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------- |
| num_workers             | Number of GPUs                                                                              |
| character_dict_path     | Customized dictionary path e.x. ppocr/utils/dict/total_dic.txt                                    |
| Architecture-Algorithm: | SVTR、PREN、Rosetta、RARE、STARNet、SRN、NRTR、CRNN、SEED、SAR                        |
| Architecture-Backbone:  | MobileNetV1Enhance、EfficientNetb3_PREN、MobileNetV3、SVTRNet、ResNetFPN、MTB、ResNet |

Start training after modification

```
cd PaddleOCR
# Need to modify train.sh --gpus parameters e.x. 3 GPUs --gpus '0,1,2'
sh train.sh
```

If you temporarily interrupt training and want to continue, use re-train.sh to resume training

```
cd PaddleOCR
# Need to modify re-train.sh --gpus parameters
sh re-train.sh
```

The saved model and training directory will be available under the output directory after the training is completed

```
my_ocr_model/
├── best_accuracy.pdopt
├── best_accuracy.pdparams
├── best_accuracy.states
├── config.yml
├── latest.pdopt
├── latest.pdparams
├── latest.states
└── train.log
```

## Predicted results by language

Using tools/test_data_predict.py to predict and calculate CERs for **simulated test image data**.

```
cd tools/
python test_data_predict.py
```

Predicted results are saved in PaddleOCR/result

## Predicted Results (CER)

Algorithm used : **SVTR** Backbone used : **MobileNetV1Enhance**

|        | Chinese Characters   | English     | POJ | mixed Hanji   |
| ------ | ------ | ------ | ------ | ------ |
| CER(%) | 3.949% | 0.166% | 2.350% | 1.908% |
| Number of characters | 12050  | 17784  | 29549  | 10138  |

## Applications

Converting trained **text recognition** models into inference models

```
cd PaddleOCR
python3 tools/export_model.py -c configs/rec/PP-OCRv3/PP-OCRv3_rec.yml -o Global.pretrained_model=output/my_ocr_model/best_accuracy  Global.save_inference_dir=./rec_inference/
```

After conversion, it will be in the PaddleOCR/rec_inference directory.
Folder Tree

```
rec_inference/
├── inference.pdiparams
├── inference.pdiparams.info
└── inference.pdmodel
```

## How to predict the whole picture (text detection model + text recognition model)

Use PaddleOCR/tools/infer/predict_system.py to make predictions about the pictures

```
#Image Path --image_dir
#Font Path --vis_font_path
cd PaddleOCR
python tools/infer/predict_system.py --det_model_dir="./det_inference" --rec_model_dir="./rec_inference" --rec_char_dict_path=./ppocr/utils/dict/total_dic.txt --vis_font_path=./test/font/ch_en.ttf --image_dir=./test/test_ch/ch.jpg
```

Prediction results are saved under the PaddleOCR/inference_results directory

## Reference

[1] [Paddleocr](https://github.com/PaddlePaddle/PaddleOCR)

[2] [Textrecognitiondatagenerator](https://github.com/Belval/TextRecognitionDataGenerator)
