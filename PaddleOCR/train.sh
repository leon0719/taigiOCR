python3 -m paddle.distributed.launch --gpus '0,1,2,3,4,5,6,7' tools/train.py -c configs/rec/PP-OCRv3/PP-OCRv3_rec.yml -o Global.pretrained_model=/workspace/PaddleOCR/Pretrained_model/best_accuracy
