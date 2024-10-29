from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            all_data.append(line)
        
file_names = [f'file {number}.txt' for number in range(1,5)]



if __name__ == '__main__':
    start = datetime.now()
    for name in file_names:
        read_info(name)
    end = datetime.now()
    print(f'{end - start} - Линейный вызов')
    
    start = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    end = datetime.now()
    print(f'{end - start} - Многопроцессный вызов')