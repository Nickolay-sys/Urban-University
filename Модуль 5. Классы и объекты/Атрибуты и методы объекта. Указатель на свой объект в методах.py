class Human:
    def __init__(self, name, age):      # Методы - функции внутри класса
        self.name = name        # Атрибуты - переменные внутри класса
        self.age = age
        self.say_info()     # в функции __init__ удобно ссылаться на функции в классе, т.к. она срабатывает срабатывает при запуске
    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')
    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')




Den = Human('Denis', 22)
Max = Human('Max', 22)

print(Den.name, Den.age)
Den.surname = 'Popov'       # можно создавать новые атрибуты
Den.age = 23        # так и изменять уже существующие
print(Den.surname, Den.age)
print(Max.name, Max.age)
Max.birthday()       