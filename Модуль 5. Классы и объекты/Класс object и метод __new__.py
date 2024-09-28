print(int.__mro__)
print(object)
class User:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        print(f'я в нью')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self,*args,**kwargs):
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