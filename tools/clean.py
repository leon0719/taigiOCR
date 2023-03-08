import re
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

def clean_line(line):
    line = line.strip('\n')
    line = re.sub(r'ñ|Ａ|Ｂ|Ｃ|Ｄ|Ｅ|Ｆ|Ｇ|Ｈ|Ｉ|Ｋ|','',line)
    text = re.sub('\s+', ' ', line).strip()
    return text

def clean(input_file:str):
    with open(input_file,'r',encoding='utf-8') as f:
        lines = f.readlines()
        
    with Pool(cpu_count()) as p:
        line_list = list(tqdm(p.imap(clean_line, lines), total=len(lines), desc="清洗語料"))
    
    with open(input_file,'w',encoding='utf-8') as f:
        for i in tqdm(line_list,desc="覆寫語料"):
            f.write(i+'\n')

if __name__ == "__main__":

    clean("TextRecognitionDataGenerator/trdg/dicts/en/en_article3.txt")