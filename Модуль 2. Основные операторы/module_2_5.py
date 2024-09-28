def get_matrix(n, m, value):        # функция с неопределённым параметром параметрами
    matrix = []     # пустой список
    for i in range(n):      # условие - для строк в пределах параметра   
        matrix.append([])       # добавляет пустой список
        for j in range(m):      # услвовие - для столбцов в пределах параметра  
            matrix[i].append(value)     # добавляет неопределённое значение
    return matrix       # возвращение полученных значений
result1 = get_matrix(2, 2, 10)      
result2 = get_matrix(3, 5, 42)      
result3 = get_matrix(4, 2, 13)      
print(result1)
print(result2)
print(result3)

class get_matrix:
    matrix = []     # пустой список
    def __init__(self, n, m, value):        # функция с неопределённым параметром параметрами
        def get_matrix():
            for i in range(n):      # условие - для строк в пределах параметра   
                self.matrix.append([])       # добавляет пустой список
            for j in range(m):      # услвовие - для столбцов в пределах параметра  
                self.matrix[i].append(value)     # добавляет неопределённое значение
            return self.matrix       # возвращение полученных значений
result1 = get_matrix(2, 2, 10)      
result2 = get_matrix(3, 5, 42)      
result3 = get_matrix(4, 2, 13)      
print(result1)
print(result2)
print(result3)

