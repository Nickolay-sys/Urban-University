from pprint import pprint
import io

"""
Подготовим файл sample4 и записав в него текст для последущеё работы
При прочтении этого файла вместо русских букв выходят не понятные символы
Это можно исправить указав что при прочтении параметр encoding уточнив что будем использовать 'utf-8'  
Так же можно заметить что выводимое кол-во больше кол-ва символов. Дело в том что выводятся именно байты
"""
name = 'sample4.txt'
file = open(name, 'r')
print(file.tell())
pprint(file.read())
print(file.tell())
file.close()

name = 'sample4.txt'
file = open(name, 'r', encoding='utf-8')
print(file.tell())
pprint(file.read())
print(file.tell())
file.close()

"""
Ещё существуют методы для проверки файлов на возможность изменить, прочитать и так далее
"""
print('\n')
name = 'sample4.txt'
file = open(name, 'r', encoding='utf-8')
print(file.writable())
print(file.readable())
print(file.seekable())
print(file.buffer)
print(file.closed)
file.close()

print(file.closed)
  