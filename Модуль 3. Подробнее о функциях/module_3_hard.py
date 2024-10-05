"""
Задание "Раз, два, три, четыре, пять .... Это не всё?":
    Наши студенты, без исключения, - очень умные ребята. 
        Настолько умные, что иногда по утру сами путаются в том, что намудрили вчера вечером.
    Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). 
        Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:
            data_structure = [
                [1, 2, 3],
                {'a': 4, 'b': 5},
                (6, {'cube': 7, 'drum': 8}),
                "Hello",
                ((), [{(2, 'Urban', ('Urban2', 35))}])
                ]
    Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
    Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
    Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур он не нашёл.
    Помогите сокурснику осуществить его задумку.
    Что должно быть подсчитано:
        Все числа (не важно, являются они ключами или значениям или ещё чем-то).
        Все строки (не важно, являются они ключами или значениям или ещё чем-то)
"""
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

def calculate_sum(structure):
    counter = 0
    for elem in structure:
        if isinstance(elem, list|tuple|set):
            counter += calculate_sum(elem)
        if isinstance(elem, dict):
            for i in elem:
                if isinstance(i, str):
                    counter += len(elem)
                if isinstance(i, int):
                    counter += i
                if isinstance(i, float):
                    counter += round(i,2)
        if isinstance(elem, str):
            counter += len(elem)
        if isinstance(elem, int):
            counter += elem
        if isinstance(elem, float):
            counter += round(elem,2)
    return counter
            
result = calculate_sum(data_structure)
print(result)