python run.py -c 200 -i dicts/ch/chinese_article.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -b 3 -ft fonts/train_font/ch/
python run.py -c 200 -i dicts/en/en_article.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -b 3 -ft fonts/train_font/en/
python run.py -c 200 -i dicts/TAI_LO/TAI_LO_corpus.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -b 3 -ft fonts/train_font/TAI_LO/
python run.py -c 200 -i dicts/POJ/POJ_corpus.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -b 3 -ft fonts/train_font/POJ/
python run.py -c 200 -i dicts/HAN_LO/HAN_LO_corpus.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -b 3 -ft fonts/train_font/HAN_LO/
