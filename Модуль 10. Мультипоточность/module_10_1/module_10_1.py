from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    
    with open(file_name, 'w', encoding='utf-8') as file:
        n = 0
        for line in range(word_count):
            n += 1
            file.write(f'Слово №{n} \n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()
    
write_words(10,'example1.txt')
write_words(30,'example2.txt')
write_words(200,'example3.txt')      
write_words(100,'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start  
print(f'Работа потоков {time_res}') 

thr_1 = Thread(target=write_words, args=(10,'example5.txt'))
thr_2 = Thread(target=write_words, args=(30,'example6.txt'))
thr_3 = Thread(target=write_words, args=(200,'example7.txt'))
thr_4 = Thread(target=write_words, args=(100,'example8.txt'))

time_start = datetime.now()

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end = datetime.now()
time_res = time_end - time_start  
print(f'Работа потоков {time_res}') 