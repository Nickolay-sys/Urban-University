class Human:
    def __init__(self, name, age):      # методы с __ __ называются dunder-методы
        self.name = name
        self.age = age
        self.say_info()
        
    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}') 
        
    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')
        
    def __len__(self):      
        return self.age
    
    def __del__(self):      # деструктор. Определяет логику при удалении объекта. Объекты существуут тдо тех пор пока есть хотя бы одна ссылка на этот объект
        print(f'{self.name} ушёл')


Den = Human('Denis', 22)
Max = Human('Max', 22)
Max.birthday()      
print(len(Den))