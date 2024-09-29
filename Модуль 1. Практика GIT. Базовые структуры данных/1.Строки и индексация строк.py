"""
Строка – это последовательность символов кодировки Unicode. Строки всегда заключаются в кавычки.
"""
name = 'Nikolay'
age = 26

# ОПЕРАЦИИ СО СТРОКАМИ
print('Hello, ' + name)     # строки можно складывать с переменными
print('Hello ' * 5)     #  если указать умножение после строки то она будет повторена n-ое кол-во раз
print(f'Hello {name}')        # чтобы упростить написание строк с перменными можно использовать f-строки
print(f'Мне {age} лет')     # в f-строках переменную можно в вписывать прямо в текст через {фигурные скобки}

#ИНДЕКСАЦИЯ СТРОК
print(name[0])      # счёт в строке начинается с нуля, соотсветсвенно индекс первого символа [0]
print(name[-1])     # при отрицательном значении индекса счёт начинается с конца
print(name[0:3])        # с помощью индексов можно вывести срез строки. Границы среза отделяются [:]. Указаный как конец среза элемент с индексом[:3] не выводится
print(name[0:3:2])      # можно указать шаг среза[:2]. Он указывается после конца среза[:3]
print(name[:3])     # если не указать начало среза отсчёт идёт с начала строки
print(name[2:])     #   если не указать конец среза отсчёт идёт до конца строки
print(name[::-1])       # без указания начала и конца среза будут выведены все символы (при отрицательном значении в обратном порядке)
        
