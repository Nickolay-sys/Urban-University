class primes:
    primes = []     # пустой список
    not_primes = []     # пустой список 
    def __init__(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        for n in numbers:       # цикл перебирает список numbers
            if n == 1:      # условие - если число n = 1 выполняет следущую строку
                continue        # пропускает выполнение последующих строк 
            #print(n)
            is_prime = True     # переменная для отметки простоты числа
            for i in range(2, n):       # вложенный цикл подбирающий делители для числа n из первого цикла
                if n % i == 0:      # если при делителе 2 или больше получается 0
                    #print(i)
                    is_prime = False        # отмечает как не соответсвующее переменной is_prime = True. Ставит флаг False
                    break       # прерывает выполнение цикла при выполненом условии
            if is_prime:        # условие - если у числа флаг True
                self.primes.append(n)        # добавляет число к списку primes
            else:       # условие - иначе выполнить следущюю строку
                self.not_primes.append(n)        # добавляет число к списку not_primes
        print(f'Primes: {self.primes}')        # вывод получившегося списка primes 
        print(f'Not Primes: {self.not_primes}')        # вывод получившегося списка not_primes 
primes()