class Human:
    head = True
    
    # def __init__(self):
    #     self.about()
    def say_hello(self):
        print('Hello')
    
class Student(Human):
    head = False
    
    def about(self):
        print('I am a student')
        
class Teacher(Human):   
    pass
        
        
human = Human()
student = Student()
teacher = Teacher()
print(human.head)
student.about()
print(student.head)
student.say_hello()
teacher.say_hello()
