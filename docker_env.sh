docker run --gpus all -it --name GPU5 -u $(id -u):$(id -g) \
    -v /home/leon/taigiOCR:/workspace/ \
    -v /nfs/TS-1635AX/WorkSpace/leon/GPU5/:/train_data/ \
    --shm-size=140g --ulimit memlock=-1 leonhilty/ocr_search:v1.0.8 /bin/bash

# -u $(id -u):$(id -g)
