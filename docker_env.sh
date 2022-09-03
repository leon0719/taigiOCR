docker run --gpus all -it --name GPU5 \
    -v /home/leon/taigiOCR:/workspace/ \
    -v /nfs/TS-1635AX/WorkSpace/leon/GPU5/train_datia:/train_data/ \
    --shm-size=120g --ulimit memlock=-1 leonhilty/ocr_search:v1.0.6 /bin/bash


# -u $(id -u):$(id -g)

