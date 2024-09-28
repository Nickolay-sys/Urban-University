numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number = int(input("Введите число - "))
list_ = []
list_1 = []
for i in numbers:
    if  i < number:
        #print(i)
        list_.append(i) 
for j in numbers:
    if  j < number:
        #print(j)
        list_1.append(j)
    #if i + j == number:
        #list_1.append
combs = []
for i in numbers:
    if  i < number:
        for j in numbers:
            if  j < number:
                if i + j == number and j != i and j >= i:
                    combs.append((i, j))
                    
#print(list_)
#print(list_1)
print(*combs)
        
#print(f"{number} - ", *list_)