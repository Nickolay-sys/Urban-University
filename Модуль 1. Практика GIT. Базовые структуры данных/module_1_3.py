"""
Практическая работа по уроку "Динамическая типизация"
Цель: написать программу для демонстрации динамической типизации.
      Создайте переменные разных типов данных:
            - Создайте переменную name и присвойте ей значение вашего имени (строка).
            - Выведите значение переменной name на экран.
            - Создайте переменную age и присвойте ей значение вашего возраста (целое число).    
            - Выведите значение переменной age на экран.
            - Перезапишите в age текущее значение переменной age + новое.
"""
name = 'Nikolay'
age = 26
is_student = True
print(f'Name: {name}'
      f'\nAge: {age}'
      f'\nNew age : {age + 1}'
      f'\nIs student: {is_student}')

class Example:
      def __init__(self, name:str, age:int, is_student:bool ) -> None:
            self.name = name
            self.age = age
            self.is_student = is_student
            print(f'Name: {self.name}'
                  f'\nAge: {self.age}'
                  f'\nNew age: {self.age + 1}'
                  f'\nIs student: {self.is_student}')
Example('Nikolay', 24, False)


