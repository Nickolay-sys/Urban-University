def func_with_params(a, b):         # если передать свои значения функция будет работать с передаными значениями
    print(a + b)
func_with_params(2, 2)


def func_with_params(a = 2, b = 2):         # если параметры указаны по умолчанию их не нужно указывать для вызова функции
    print(a + b)
func_with_params()


def func_with_params(a, b = 3):         # параметр указаный по умолчанию должен идти после не указаного 
    print(a + b)
func_with_params(2, 3)


def func_with_params(a, b = 2, c = 3):         # параметры по умолчанию так же можно изменить
    print(a + b + c)
func_with_params(3, 5)


def func_with_params(a, b = 2, c = []):         # если указать по умолчанию список, то новые параметры будут вноситься в него
    c.append(a)
    print(c)
func_with_params(3)
func_with_params(3)


def func_with_params(a, b = 2, c = None):         # если добавить условие проверки параметра на соответсвие значения по умолчанию, то список будет перопределяться
    if c is None:
        c = []
        c.append(a)
    print(c)
func_with_params(3)
func_with_params(4)