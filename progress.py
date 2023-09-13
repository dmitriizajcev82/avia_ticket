import random

from tqdm import tqdm
import time

def print_progress_bar():
    print_out = ['Ищем данные....','Небольшое ожидание....']
    random_print_out = random.choice(print_out)
    for i in tqdm(range(104),
                  desc=random_print_out,
                  ascii=False, ncols=75):
        time.sleep(0.01)


    print("Готово!")

