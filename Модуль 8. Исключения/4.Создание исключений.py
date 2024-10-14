"""
Для чего нужны raise:
    1.Чтобы генерить исключения,когда фунции передаются некорректные аргументы
    2.Если достигнута точка, при котром дальнейшее исполнение невозможно или бесмысленно
    3.Если обнаружена ошибка в логике кода, которой не должно быть при правильной работе 
"""
# def greet_person(person_name):
#     if person_name == 'Nikolay':
#         raise Exception('We dont love you Nikolay')
#     print(f'Hello, {person_name}')
    
# greet_person('Student')
# greet_person('Nikolay')


# try:
#     raise NameError('Hello Tam')
# except NameError as exc:
#     print(f'Exeption type {type(exc)} gone by. Its params {exc.args}')
#     raise


class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

def f(a,b):
    if b == 0:
        raise ProZero('Divizion by zero is imposible', {'a': a, 'b':b})
    return a / b

try:
    result = f(10,0)
except ProZero as e:
    print('Today is not very good day. We got a bug')
    print(f'Message - {e.message}')
    print(f'Extra info - {e.extra_info}')