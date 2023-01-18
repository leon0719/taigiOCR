# en
python tools/infer/predict_system.py \
--det_model_dir="./det_inference" \
--rec_model_dir="./rec_inference/" \
--rec_char_dict_path=./ppocr/utils/dict/vocab.txt \
--vis_font_path=./test_image/test_font/en_ch_font.ttf \
--image_dir=./test_image/en \
--use_gpu False \
--draw_img_save_dir ./inference_results/en
#HAN_LO
python tools/infer/predict_system.py \
--det_model_dir="./det_inference" \
--rec_model_dir="./rec_inference/" \
--rec_char_dict_path=./ppocr/utils/dict/vocab.txt \
--vis_font_path=./test_image/test_font/Hanji_font.ttf \
--image_dir=./test_image/HAN_LO \
--use_gpu False \
--draw_img_save_dir ./inference_results/HAN_LO
#Hanji
python tools/infer/predict_system.py \
--det_model_dir="./det_inference" \
--rec_model_dir="./rec_inference/" \
--rec_char_dict_path=./ppocr/utils/dict/vocab.txt \
--vis_font_path=./test_image/test_font/Hanji_font.ttf \
--image_dir=./test_image/Hanji \
--use_gpu False \
--draw_img_save_dir ./inference_results/Hanji
#POJ
python tools/infer/predict_system.py \
--det_model_dir="./det_inference" \
--rec_model_dir="./rec_inference/" \
--rec_char_dict_path=./ppocr/utils/dict/vocab.txt \
--vis_font_path=./test_image/test_font/POJ_font.ttf \
--image_dir=./test_image/POJ \
--use_gpu False \
--draw_img_save_dir ./inference_results/POJ