python run.py -c 10 -f 48 -i dicts/ch/test.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/Hanji -fd fonts/ch/
python run.py -c 4 -f 48 -i dicts/en/test.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/en -fd fonts/en/
python run.py -c 9 -f 48 -i dicts/TAI_LO/test.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/POJ -fd fonts/TAI_LO/
python run.py -c 20 -f 48 -i dicts/POJ/test.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/POJ -fd fonts/POJ/
python run.py -c 23 -f 48 -i dicts/HAN_LO/test.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/HAN_LO -fd fonts/HAN_LO/
python run.py -c 12 -f 48 -i dicts/jp/test.txt -t $(cat /proc/cpuinfo | grep "processor" | wc -l) -id images/Hanji/ -fd fonts/jp/
