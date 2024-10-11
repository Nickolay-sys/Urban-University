"""

"""
import os

print('Текущая дериктория: ', os.getcwd())
if os.path.exists('first'):
    os.chdir('first')
else:
    os.mkdir('first')
    os.chdir('first')
print('Текущая дериктория: ', os.getcwd())
# os.makedirs(r'second\ third')
print(os.listdir())
for i in os.walk('.'):
    print(i)
os.chdir(r'D:\Urban University\Модуль 7. Работа с файлами и форматированный вывод')
print('Текущая дериктория: ', os.getcwd())
files = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(files)
os.startfile(files[11])
print(os.stat(files[3]).st_size)