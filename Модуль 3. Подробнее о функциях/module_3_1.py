"""
Задача "Счётчик вызовов":
    Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. 
    К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
    Давайте реализуем данную фишку самостоятельно!
    Вам необходимо написать 3 функции:
        Функция count_calls подсчитывающая вызовы остальных функций.
        Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
        Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. 
         Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
"""
calls =  0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    lower_list_to_search = [s.lower() for s in list_to_search]
    if string.lower() in lower_list_to_search:
        return True
    else:
        return False
    
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

class Example:
    global calls
    def __init__(self, string, list_to_search):
        self.string = string
        self.list_to_search = list_to_search
        print(len(self.string), self.string.upper(), self.string.lower())
        if self.string in self.list_to_search:
            print(True)
        else:
            print(False)
Example('Owl',['cat','dog'])
        
