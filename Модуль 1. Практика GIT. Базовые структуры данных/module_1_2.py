"""
Практическое задание по теме "Переменные".
Задача: напишите 4 переменных которые буду обозначать следующие данные:
      1.Количество выполненных ДЗ (запишите значение 12)
      2.Количество затраченных часов (запишите значение 1.5)
      3.Название курса (запишите значение 'Python')
      4.Время на одно задание (вычислить используя 1 и 2 переменные)
Выведите на экран(в консоль), используя переменные, следующую строку:
      Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

"""
course_name = 'Python'
total_tasks = 20
houres_spent = 2.4
print(f'Курс програмирования на языке: {course_name}, '
      f'всего задач: {total_tasks}, '
      f'затраченно часов {houres_spent}, '
      f'среднее время выполнения {houres_spent/total_tasks} часа')

class Example:
      def __init__(self, course_name, total_tasks, houres_spent):
           self.course_name = course_name
           self.total_tasks = total_tasks
           self.houres_spent = houres_spent
           print(f'Курс:  {self.course_name}' 
                 f'\nВсего задач: {self.total_tasks}'
                 f'\nЗатрачано часов: {self.houres_spent}'
                 f'\nСреднее время выполнения  {self.houres_spent / self.total_tasks} часа')
            
Example('Python', 12, 1.5 )

