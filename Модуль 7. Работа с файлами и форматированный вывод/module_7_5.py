import os
import time

directory = '.'

os.walk(directory)
os.path.join(directory)
os.path.getmtime(directory)
os.path.getsize(directory)
os.path.dirname(directory)

for root,dirs,files in os.walk(directory):
    for file in files:
        filepath = os.path.join(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(file)
        
print(f'Обнаружен файл: {file}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')