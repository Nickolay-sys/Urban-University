"""
Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"
Цель: написать программу на языке Python, используя Pycharm, для работы с неизменяемыми и изменяемыми объектами.
   1. Задайте переменные разных типов данных:
      - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
      - Выполните операции вывода кортежа immutable_var на экран.
   2. Изменение значений переменных:
      - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
   3. Создание изменяемых структур данных:
      - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
      - Измените элементы списка mutable_list.
      - Выведите на экран измененный список mutable_list.
"""

immutable_var = (1,2,3,4)
mutable_list = [1,2,3,4]
print(f'Immutable tuple: {immutable_var}')
mutable_list.append(immutable_var)
print(f'Mutable list: {mutable_list}')
mutable_list.extend('abcd')
print(f'Mutable list: {mutable_list} modified')

class Example:
   def __init__(self,immutable_var,mutable_list):
      self.immutable_var = immutable_var
      self.mutable_list = mutable_list
      print(f'Immutable tuple: {self.immutable_var}')
      self.mutable_list.append(self.immutable_var)
      print(f'Mutable list: {self.mutable_list}')
      self.mutable_list.extend('abcd')
      print(f'Mutable list: {self.mutable_list} modified')
      
Example((1,2,3,4,5,6,7,8,9),[9,8,7,6,5,4,3,2,1])

