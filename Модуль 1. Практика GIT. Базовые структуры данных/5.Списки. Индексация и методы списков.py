"""
Список - упорядоченный набор элементов, каждый из которых имеет свой индекс
"""
food = ['apple','coconut','banana']

"""
Можно работать с каждым эелементом списка по отдельности
"""
print(food[0])
print(food[1])
print(food[2])

"""
В том числе изменять элементы
"""
food[0] = 'peach'
print(food)

"""
В список с помощью методов можно добавлять новые элементы с разным типом данных и удалять их 
"""
food.append(True)       # добавить к концу списка
print(food)
food.extend('string')       # # добавляет к списку последовательность символов
print(food)
food.extend(['string', 2])      # если добавить квадратные скобки, то есть новый список, то сиволы будут объеденены 
print(food)
food.remove('banana')
print(food)

"""
Также маожно использовать и команды
"""
print('coconut' in food)
print('coconut' not in food)
print(food[0:2])
print(food[0:2:2])