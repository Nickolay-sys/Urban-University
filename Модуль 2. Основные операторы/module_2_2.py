"""
Задача "Все ли равны?":
    На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
    Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
    Пункты задачи:
        Если все числа равны между собой, то вывести 3
        Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
        Если равных чисел среди 3-х вообще нет, то вывести 0
"""
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and first == third or second == third:
    print(f'Кол-во равных друг другу чисел - 3')
elif first == second or first == third or second == third:
    print(f'Кол-во равных друг другу чисел - 2')
elif first != second or first != third or second != third:
    print(f'Кол-во равных друг другу чисел - 0')
    
class Equals:
    def __init__(self,first,second,third):
        self.first = first
        self.second = second
        self.third = third
        if first == second and first == third or second == third:
            print(f'Кол-во равных друг другу чисел - 3')
        elif first == second or first == third or second == third:
            print(f'Кол-во равных друг другу чисел - 2')
        elif first != second or first != third or second != third:
            print(f'Кол-во равных друг другу чисел - 0')
Equals(int(input('Введите первое число: ')),
       int(input('Введите второе число: ')),
       int(input('Введите третье число: ')))
