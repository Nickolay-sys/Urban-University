# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
result_1 = list(map(lambda x,y: x == y, first,second))
print(result_1)


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for line in data_set:
                file.write(f'{line}\n')
        
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



# Метод __call__:
from random import choice
class MysticBall():
    def __init__(self, *words):
        self.words = words
        
    def __call__(self):
        result = choice(self.words)
        return result
    
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
