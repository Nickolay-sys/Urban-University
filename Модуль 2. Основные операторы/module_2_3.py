"""
Задача "Нули ничто, отрицание недопустимо!":
    Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    Нужно выписывать из этого списка только положительные числа до тех пор, 
    пока не встретите отрицательное или не закончится список (выход за границу).
    Пункты задачи:
        Запишите исходный список в переменную my_list.
        Напишите цикл while с соответствующими задаче условиями.
        Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.
"""
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0       # переменная для условий цикла
while i < len(my_list):     # сравнение индекса и длинны строки не даёт выйти за его границу и позволяет повторять цикл
    if my_list[i] < 0:      # если полученое по индексу значение будет меньше 0 то будет выполенно следущая строка
        break       # прерывает цикл
    if my_list[i] > 0:      # если полученое по индексу значение будет больше 0 то будет выполенно следущая строка
        print(my_list[i])       # вывод числа
    i += 1      # сдвигает индекс на указаный шаг
    
print(' ')

class List:
    def __init__(self,my_list):
        self.my_list = my_list
        i = 0
        while i <len(my_list):
            if my_list[i] < 0:
                break
            if my_list[i] > 0:
                print(my_list[i])
            i += 1
List([78, 629, 2322, 0, -13, 0, 99, -5, 9, 8, 7, -6, 5])
        