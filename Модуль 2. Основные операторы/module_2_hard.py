"""
Задание "Слишком древний шифр":
    Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли 
        вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
    К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
    Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.
    В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
    К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, 
        где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).
    Во вторую вставку нужно было написать те пары чисел друг за другом, 
        чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number = int(input("Введите число - "))
list_ = []
list_1 = []
for i in numbers:
    if  i < number:
        list_.append(i) 
for j in numbers:
    if  j < number:
        list_1.append(j)
combs = []
for i in numbers:
    if  i < number:
        for j in numbers:
            if  j < number:
                if i + j == number and j != i and j >= i:
                    combs.append((i, j))
print(*combs)

class Decoder:
    number = int(input("Введите число - "))
    list_ = []
    list_1 = []
    def __init__(self,numbers):
        self.numbers = numbers
        for i in numbers:
            if  i < self.number:
                self.list_.append(i) 
        for j in numbers:
            if  j < self.number:
                self.list_1.append(j)
        comb = []
        for i in numbers:
            if  i < self.number:
                for j in numbers:
                    if  j < self.number:
                        if i + j == self.number and j != i and j >= i:
                            comb.append((i, j))
        print(*comb)
Decoder([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])