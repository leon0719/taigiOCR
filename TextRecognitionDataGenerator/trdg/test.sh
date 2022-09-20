python run.py -c 200 -d 3 -f 48 -i dicts/ch/ch_article2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/Hanji -fd fonts/ch/
python run.py -c 200 -d 3 -f 48 -i dicts/en/en_article2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/en -fd fonts/en/
python run.py -c 200 -d 3 -f 48 -i dicts/TAI_LO/TAI_LO_corpus2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/POJ -fd fonts/TAI_LO/
python run.py -c 200 -d 3 -f 48 -i dicts/POJ/POJ_corpus2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/POJ -fd fonts/POJ/
python run.py -c 200 -d 3 -f 48 -i dicts/HAN_LO/HAN_LO_corpus2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/HAN_LO -fd fonts/HAN_LO/
python run.py -c 200 -d 3 -f 48 -i dicts/jp/jp_corpus2.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/Hanji/ -fd fonts/jp/
