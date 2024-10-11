"""
Виды форматирования строк:
    1.Конкатенация - сложение строк
    2.Форматирование с использованием символа %. Принимает только 1 аргумент который может быть кортежом
    3.Метод Format
    4.F-строка
"""
# Конкатенация
print('Hello, ' + 'world!')

# Форматирование с использованием символа %
print('My name %s, i am %s years olds'%('Nikolay', 26))

# Метод Format
print('I student in {}'.format('Urban University'))
print('I student in {} {}'.format('Urban','University'))
print('I student in {0} {1} {0}'.format('Urban', 'University'))
print('I student in {title} {postfix}'.format(title='Urban',postfix='University'))

# F-строка
print(f'{"Urban"} is best university')