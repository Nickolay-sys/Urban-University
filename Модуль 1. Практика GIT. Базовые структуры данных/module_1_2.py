course_name = 'Python'
total_tasks = 20
houres_spent = 2.4
print(f'Курс програмирования на языке: {course_name}'
      f'\nВсего задач: {total_tasks}'
      f'\nЗатраченно часов {houres_spent}'
      f'\nСреднее время выполнения {houres_spent/total_tasks} часа')

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

