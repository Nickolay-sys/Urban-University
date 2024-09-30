"""
Задача "Всё не так уж просто":
    Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    Используя этот список составьте второй список primes содержащий только простые числа.
    А так же третий список not_primes, содержащий все не простые числа.
    Выведите списки primes и not_primes на экран(в консоль).
    Пункты задачи:
        1.Создайте пустые списки primes и not_primes.
        2.При помощи цикла for переберите список numbers.
        3.Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
        4.Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
        5.В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes 
            в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
        6.Выведите списки primes и not_primes на экран(в консоль).
"""
primes = []     # пустой список
not_primes = []     # пустой список 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for n in numbers:       # цикл перебирает список numbers
    if n == 1:      # условие - если число n = 1 выполняет следущую строку
        continue        # пропускает выполнение последующих строк 
    is_prime = True     # переменная для отметки простоты числа
    for i in range(2, n):       # вложенный цикл подбирающий делители для числа n из первого цикла
        if n % i == 0:      # если при делителе 2 или больше получается 0
            is_prime = False        # отмечает как не соответсвующее переменной is_prime = True. Ставит флаг False
            break       # прерывает выполнение цикла при выполненом условии
    if is_prime:        # условие - если у числа флаг True
        primes.append(n)        # добавляет число к списку primes
    else:       # условие - иначе выполнить следущюю строку
        not_primes.append(n)        # добавляет число к списку not_primes
print(f'Primes: {primes}')        # вывод получившегося списка primes 
print(f'Not Primes: {not_primes}')        # вывод получившегося списка not_primes 

class Primes:
    primes = []
    not_primes = []
    def __init__(self):
        numbers = [100, 101, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]
        for n in numbers:
            if n == 1:
                continue
            is_prime = True     
            for i in range(2, n):     
                if n % i == 0:     
                    is_prime = False        
                    break       
            if is_prime:        
                self.primes.append(n)     
            else:    
                self.not_primes.append(n)      
        print(f'Primes: {self.primes}')        
        print(f'Not Primes: {self.not_primes}')        
Primes()