[English](README.md) | Chinese

# 主要功能

辨識中、英、漢羅台文、白話字、全羅等等圖片文字並儲存成文字檔

![image](images/result_ch.jpg "中")

![image](images/result_en.jpg "英")

![image](images/result_HAN_LO.jpg "漢羅")

![image](images/result_POJ.jpg "白話字")

# 安裝環境

下載 repository

```
git clone https://github.com/leon0719/taigiOCR.git
```

利用 Docker image 來建立環境，安裝函式庫 、 CUDA 及 CUDA Toolkit

```
#建立 資料夾儲存圖片
mkdir img_data

docker run --gpus all -it --name OCR_ENV -v /path/to/taigiOCR:/workspace/ -v /path/to/img_data:/train_data/ --shm-size=120g --ulimit memlock=-1 leonhilty/ocr_search:v1.0.8 /bin/bash

```

確認進入 Docker 環境

![image](/images/Docker_env.jpg "Docker環境")

## 產生 DATASET

使用 tools/train_test_split.py 生成 中、英、白話字、漢羅、台羅等文字圖片並切割訓練(90%)驗證(10%)，
與模擬的測試資料

```
cd tools/
python get_data.py  # 預設 -c 400000 圖片數量
```

生成結果

![image](images/ch.png "中")
![image](images/en.jpg "英")
![image](images/POJ.jpg "白話字")
![image](images/TAI_LO.jpg "台羅")
![image](images/HAN_LO.jpg "漢羅")

資料夾樹狀圖

```
/train_data/
    (模擬測試資料)
    └── train_data
        ├── test (驗證集 Img)
        ├── test_label.txt (驗證集 Label)
        ├── train (訓練集 Img)
        └── train_label.txt (訓練集 Label)
```

## 如何訓練

修改 PaddleOCR/configs/rec/PP-OCRv3/PP-OCRv3_rec.yml 設定檔

|                         | 修改為                                                |
| ----------------------- | ----------------------------------------------------- |
| num_workers             | GPU 個數                                              |
| character_dict_path     | 自定義字典路徑 e.x. ppocr/utils/dict/total_dic.txt     |


修改後即可開始訓練

```
cd PaddleOCR
# 需修改 train.sh --gpus 參數 e.x. 3張GPU --gpus '0,1,2'
sh train.sh
```

若暫時中斷訓練想繼續訓練可使用 re-train.sh 恢復訓練

```
cd PaddleOCR
# 需修改 re-train.sh --gpus 參數
sh re-train.sh
```

訓練完成後在 output 目錄下會有保存後的模型與訓練目錄

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

## 各個語言預測結果

使用 tools/Real_Test_predict.py 對**測試圖片資料**進行預測並計算 CER

```
cd tools/
python Real_Test_predict.py
```

預測結果保存在 PaddleOCR/result 中

## 應用

將訓練好的**文字辨認**模型轉換成推理模型

```
cd PaddleOCR
python3 tools/export_model.py -c configs/PP-OCRv3_rec.yml -o Global.pretrained_model=output/my_ocr_model/best_accuracy  Global.save_inference_dir=./rec_inference/
```

轉換過後會在 PaddleOCR/rec_inference 目錄下
資料夾樹狀圖

```
rec_inference/
├── inference.pdiparams
├── inference.pdiparams.info
└── inference.pdmodel
```

## 如何預測整張圖片 (文字偵測模型+文字辨認模型)

使用 PaddleOCR/tools/infer/predict_system.py 對圖片進行預測

```
#選擇想要預測的圖片路徑 --image_dir
#字型路徑 --vis_font_path
cd PaddleOCR
sh final_infere.sh
```

預測結果會存在 PaddleOCR/inference_results 目錄下

## Reference

[1] [Paddleocr](https://github.com/PaddlePaddle/PaddleOCR)

[2] [Textrecognitiondatagenerator](https://github.com/Belval/TextRecognitionDataGenerator)
