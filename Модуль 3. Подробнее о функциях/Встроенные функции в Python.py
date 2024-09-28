# int()  --> int(input())
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()
salary = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
print(round(sum(salary)/len(salary), 2), ' - средняя зарплата в компании')          # round - окргулить до указаного числа после запятой
print(round(max(salary), 2), ' - максимальная зарплата в компании')         # max - максимальное значение
print(round(min(salary), 2), ' - минимальная зарплата в компании')          # min - минимальное значение

names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = dict(zip(names, salary))           # zip - возвращает указаные параметры как объект
print(zipped['Денис'], '- зарплата Дениса')