docker run --gpus all -it --name GPU4 -u $(id -u):$(id -g) \
    -v /home/leon/taigiOCR:/workspace/ \
    -v /nfs/TS-1635AX/WorkSpace/leon/GPU4/:/train_data/ \
    --shm-size=140g --ulimit memlock=-1 leonhilty/ocr_search:v1.0.8 /bin/bash

# -u $(id -u):$(id -g)
