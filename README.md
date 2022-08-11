# OCR 操作流程

如何利用 OCR 辨識漢羅台文、白話字、全羅等等語言

## 安裝環境

下載 repository

```
git clone https://github.com/leon0719/OCR.git
```

利用 Docker image 來建立環境，安裝對應的 CUDA 及 CUDA Toolkit

```
docker run --gpus all -it --name OCR_ENV -v /path/to/OCR/:/workspace/ -v /path/to/img_train_data/:/train_data/ --shm-size=120g --ulimit memlock=-1 leonhilty/ocr_search:v1.0.6 /bin/bash
```

確認進入 Docker 環境

![image](/images/Docker_env.jpg "Docker環境")

## 產生 DATASET

使用 tools/train_test_split.py 生成 中、英、日、白話字、漢羅、台羅等文字圖片並切割訓練(90%)驗證(10%)，
與模擬的測試資料

```
cd tools/
python3 python train_test_split.py
```

生成後資料夾結構為
/train_data/
├── test_ch
├── test_en
├── test_HAN_LO
├── test_jp
├── test_POJ
├── test_TAI_LO
└── train_data
├── test
├── train
├── test_label.txt
└── train_label.txt
