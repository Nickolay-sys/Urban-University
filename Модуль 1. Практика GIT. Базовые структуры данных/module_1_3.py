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


