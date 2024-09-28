class Human:
    head = True
    _legs = True
    __arms = True
    
    def say_hello(self):
        print('Hello')
    
    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)
    
class Student(Human):
    pass

    # def about(self):
    #     print('I am a student')
    
        
class Teacher(Human):   
    pass
        
human = Human()
human.about()

student = Student()
student.about()

# print(dir(human))
print(student._Human__arms)