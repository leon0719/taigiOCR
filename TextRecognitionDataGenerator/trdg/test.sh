python run.py -c 200 -i dicts/ch/chinese_article.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -b 3 -fd fonts/train_font/ch/ --output_dir ../../test/test_img
python run.py -c 200 -i dicts/en/en_article.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -b 3 -fd fonts/train_font/en/ --output_dir ../../test/test_img
python run.py -c 200 -i dicts/TAI_LO/TAI_LO_corpus.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -b 3 -fd fonts/train_font/TAI_LO/ --output_dir ../../test/test_img
python run.py -c 200 -i dicts/POJ/POJ_corpus.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -b 3 -fd fonts/train_font/POJ/ --output_dir ../../test/test_img
python run.py -c 200 -i dicts/HAN_LO/HAN_LO_corpus.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -b 3 -fd fonts/train_font/HAN_LO/ --output_dir ../../test/test_img
