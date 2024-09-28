import math
from module3 import *

d = 7
def square(x):
    d = x ** 2
    def even(x):
        nonlocal d
        d = x / 2
        if d % 2 == 0:
            print("Чётное")
        else:
            print("Нечётное")
    even(x)
    return d


a = 5
b = square(4)
print(a)
print(b)
print(globals())
# Существует всего 4 области видимости : голбальные, локальные, встроенные(импорты и т.д), объемлющие(фунцкция внутри функции)