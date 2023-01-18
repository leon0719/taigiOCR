python3 -m paddle.distributed.launch --gpus '0,1,2,3,4,5,6' tools/train.py \
-c configs/PP-OCRv3_rec.yml \
-o Global.pretrained_model=/workspace/PaddleOCR/Pretrained_model/en_pretrained/best_accuracy
