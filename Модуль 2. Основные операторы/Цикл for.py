for i in 1, 2, 3, 4:
    print(i)        # последовательно выведет элементы указаные в условии цикла
    print("ok")     # выведет указанную строку при выполнении условия цикла
    
for i in "Hello":
    print(i)        # последовательно выведет элементы указаные в условии цикла
    
   
list_ = ["one", "two", "three"]
for i in list_:
    print(i)        # работает и со списками
    if i == "three":        # можно работать с отдельными элементами списка
        list_.remove(i)
print(list_)


for i in range(5):      # возвращает последовательность чисел от нуля до указанного числа. Последний элемент не входит в последовательность
    print(i)
for i in range(len(list_)):     # функция len вовращает длину элемента указанного в скобках
    list_[i] = " :( "
    print(list_[i])
print(list_)

list_2 = [2, 3, 4, 5, 1]
sum_  = 0
for i in range(len(list_2)):
    sum_ += list_2[i]
print(sum_)


for i in range(1, 11):      # функция range принимает всего три команды: start, stop, step i = 1
    for j in range(1, 11):      # полсе выполнения команды повторяет её пока не пройдут все элементы полседовательности i
        print(f"{i} x {j} = {i * j}")       # полсе выполнения команды повторяет её пока не пройдут все элементы полседовательности j


dict_ = {"a": 1, "b": 2, "c": 3}
for i in dict_:     # можно работать со словарями
    print(i, dict_[i])
for i, k in dict_.items():
    print(i, k)
    