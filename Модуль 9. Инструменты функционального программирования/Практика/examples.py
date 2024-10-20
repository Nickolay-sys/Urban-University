#1
animal = 'Кот'
animals = ['Заяц', 'Кот','Собака']

def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal
    return repeat

test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
print(test_2(animal))

#2
repetions = [gen_repeat(n) for n in range(1,4)]
print(repetions)

result = [func(animal) for func in repetions]
print(result)

#3
fin_result = [func(x) for func in repetions for x in animals]
print(fin_result)

fin_result_2 = [func(x) for x in animals for func in repetions]
print(fin_result_2)

#4
def memorize_func(f):
    mem = {}
    
    def wrapper(*args):
        print(f'Выполнение функции с аргументами={args}внутренняя память={mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась,  ответ = {mem[args]}'
        else:
            return f'Функия уже была выполнена раньше, ответ = {mem[args]}'
    return wrapper

@memorize_func   
def func(a,b):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a ** b

print(func(3,5),'\n')
print(func(3,4),'\n')
print(func(3,2),'\n')
print(func(3,5),'\n')
print(func(3,4),'\n')
print(func(3,5),'\n')