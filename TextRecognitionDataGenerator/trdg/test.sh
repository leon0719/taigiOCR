python run.py -c 200 -i dicts/ch/ch_article2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/Hanji -fd fonts/train_font/ch/ --output_dir /home/leon/python_test/test/test_img
# python run.py -c 200 -i dicts/en/en_article2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/en -fd fonts/train_font/en/ --output_dir /home/leon/python_test/test/test_img
python run.py -c 200 -i dicts/TAI_LO/TAI_LO_corpus2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/POJ -fd fonts/train_font/TAI_LO/ --output_dir /home/leon/python_test/test/test_img
python run.py -c 200 -i dicts/POJ/POJ_corpus2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/POJ -fd fonts/train_font/POJ/ --output_dir /home/leon/python_test/test/test_img
python run.py -c 200 -i dicts/HAN_LO/HAN_LO_corpus2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/HAN_LO -fd fonts/train_font/HAN_LO/ --output_dir /home/leon/python_test/test/test_img
