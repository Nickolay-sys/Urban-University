"""
Стек  в Python - это линейная структура данных, вкоторой данные расположены объектами друг над другом
    Он хранит данные в режиму LIFO(Last In First Out)
Исключения в функциях спускаются по сетке вызовов функии пока не будет перехвачено
"""

def f1(number):
    return 10/number

def f2():
    print('What are lovely day')
    result_f1 = f1(0)
    return result_f1

try:
    total = f2()
    print(total)
except ZeroDivisionError as exc:
    print(f'Something gone wrong - {exc}')

print('\n')

def f3():
    summ = 0
    for i in range(-2,2,1):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'There was {exc}')
    return summ 

try:
    total = f3()
    print(total/0)
except ZeroDivisionError as exc:
    print(f'Something gone wrong - {exc}')