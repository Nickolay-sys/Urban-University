def print_params(*params):      # *args - одна звёздочка используется для запаковки и распоковки позиционных параметров с одним элементом: списки, кортежи и тд
    print(params)       # при вызове фунции указаные параметры будут упакованы в кортеж
print_params(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def print_params(*params):
    print(*params)      # при вызове функции указаные параметры будут распакованы
print_params(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def print_params(a,b,c):
    print(a,b,c)
list_ = [1,2,3]
print_params(list_,2,3)     # список занимает место одного парматра если его не распаковать

def print_params(a,b,c):
    print(a,b,c)
list_ = [1,2,3]
print_params(*list_)        # при распаковке значения из списка занимают места всех параметров. Обязательно соответсвия кол-ва параметров и значений внутри списка

def print_params(a,b,c):
    print(a,b,c)
list_ = [1,2]
print_params(1,*list_)      # можно заменять разные позиционные параметры

def print_params(a,b,c):
    print(a,b,c)
dict_ = {'a':1,'b':2,'c':3}
print_params(**dict_)       # при распаковке словарей важно чтобы названия ключей совпадали с названиями параметров если они указаны   

def print_params(**kwargs):     # **kwargs - две звёздочки используются для именованных параметров. В Pyton одна коллекция - словари
    print(kwargs)
dict_ = {'a':1,'b':2,'c':3}
print_params(**dict_)

def print_params(**kwargs):
    for key in kwargs:      # можно вывести ключ
        print(key)      
dict_ = {'a':1,'b':2,'c':3}
print_params(**dict_)

def print_params(**kwargs):
    for key, value in kwargs.items():       # можно вывести ключ и значение
        print(key, value)       
dict_ = {'a':1,'b':2,'c':3}
print_params(**dict_)

def print_params(a,b,c):
    print(a,b,c)
list_ = [1,2]
dict_ = {'c':3}
print_params(*list_, **dict_)       # можно комбинировать выводы
    