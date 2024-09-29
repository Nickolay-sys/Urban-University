"""
Практическая работа по уроку "Организация программ и методы строк".
Цель: написать программу на языке Python с использованием Pycharm для работы с методами строк и организации программ.
    1. Организуйте программу:
        Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
        Вывести количество символов введённого текста
    2. Работа с методами строк:
        Используя методы строк, выполните следующие действия:
        Выведите строку my_string в верхнем регистре.
        Выведите строку my_string в нижнем регистре.
        Измените строку my_string, удалив все пробелы.
        Выведите первый символ строки my_string.
        Выведите последний символ строки my_string.
"""
my_string = input()
print(f'{len(my_string)}')
print(f'{my_string.upper()}')
print(f'{my_string.lower()}')
print(my_string.replace(' ',''))
print(f'{my_string[0]}')
print(f'{my_string[-1]}')

class Example:
    def __init__(self, my_string):
        self.my_string = my_string
        print(f'{len(self.my_string)}')
        print(f'{self.my_string.upper()}')
        print(f'{self.my_string.lower()}')
        print(self.my_string.replace(' ',''))
        print(f'{self.my_string[0]}')
        print(f'{self.my_string[-1]}')    
Example(input())

