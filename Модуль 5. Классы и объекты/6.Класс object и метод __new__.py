print(int.__mro__) # атрибут mro позволяет посмотреть цепочку наследования для этого класса
print(object)
class User:
    __instance = None
    
    def __new__(cls, *args, **kwargs):  # этот метод срабатывает перед созданием объекта класса
        print(f'я в нью')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self,*args,**kwargs):  # этот метод срабатывает после создания объекта класса
        print(f'я в ините')
        self.args = args
        # self.name = kwargs.get('name')
        # self.age = kwargs.get('age')
        for key, values in kwargs.items():
            setattr(self, key, values)
        
other = [1,2,3]
user = {'name':'den', 'age':25, 'gender':'male'}
        
user1 = User(*other, **user)
# user2 = user()
# print(id(user1), id(user2))
print(user1.args)
print(user1.name)
print(user1.age)
print(user1.gender)