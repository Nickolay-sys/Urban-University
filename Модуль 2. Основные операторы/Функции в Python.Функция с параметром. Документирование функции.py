def say_hello():        # функция и её название. Бывают обычными, принимающими, возвращаемыми и анонимными. Это обычная функция
    print("Hello")      # содержимое функции  
say_hello()     # использование функции
say_hello()     # можно вызвать несограниченное кол-во раз

def say_hello(name):     # принимающая функция
    print("Hello", name)        # вывод функции с принимаемым параметром
say_hello("Nick")      # меняет параметр функции на указаный в скобках
say_hello("Max")        # меняет параметр функции на указаный в скобках
say_hello("Denis")      # меняет параметр функции на указаный в скобках

import random       # встроенная библиотека для генерации случайных чисел 
def lottery():      # возвращающая функция
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]       # список
    win = random.choice(tickets)        # переменая определёная указаной командой
    return win      # команда для возвращения данных и окночания выполнения функции
win = lottery()     # определяет переменую параметра функции
print(win)      # вывод получившейся переменой

import random
def lottery(mon, thue):     # можно придать функции значение
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)        # после выполнения команды уберёт выбраное число из списка
    win2 = random.choice(tickets)
    print(mon, thue)
    return win1, win2
win1, win2 = lottery("mon", "thue")     # определяет переменую параметра функции
print(win1, win2)       # вывод параметра функции и получившейся переменой

import random
def lottery(*args, **kwargs):       # если неизвестно кол-во приниаемых параметров используются эти *args для обычных, **kwargs для именованных
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(*args)
    return win1, win2
win1, win2 = lottery(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(win1, win2)

def test(a = 2, b = True):      # параметр по умалчанию
    print(a, b)
test(False, "ok")       # переназначеные параметры
test([1, 2])        # список является одним параметром
test(*[1, 2])       # * распаковывает список
test({"a": [3,4]})      # словарь является одним параметром
test(**{"a": [3,4]})        # ** распаковывает список