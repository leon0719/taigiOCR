# OCR 操作流程

如何利用 OCR 辨識漢羅台文、白話字、全羅等等語言

## 安裝環境

利用 Docker 映像檔 來建立環境，安裝對應的 CUDA 及 CUDA Toolkit

```
docker run --gpus all -it --name OCR_ENV -v /path/to/OCR/:/workspace/ -v /path/to/img_train_data/:/train_data/ --shm-size=120g --ulimit memlock=-1 leonhilty/ocr_search:v1.0.6 /bin/bash
```

確認進入 Docker 環境

![image](/images/Docker_env.jpg "Docker環境")
