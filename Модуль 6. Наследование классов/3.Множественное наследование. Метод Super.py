"""
super() - функция вызывающая методы родительского класса в дочернем классе.
При наследовании можно не ограничиваться одним родительским классом
"""
class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()
        
    def info(self):
        print(f'Hello. My name is {self.name}')


class StudentGroup:
    def __init__(self, group):
        self.group = group
        
    def about(self):
        print (f'{self.name} studying in {self.group}')

    
class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()


# human = Human('Denis')
# print(human.name)
student = Student('Max', 'Urban', 'Python 1')

