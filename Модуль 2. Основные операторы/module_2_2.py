class equals:
    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    third = int(input('Введите третье число: '))
    if first == second and first == third or second == third:
        print(f'Кол-во равных друг другу чисел - 3')
    elif first == second or first == third or second == third:
        print(f'Кол-во равных друг другу чисел - 2')
    elif first != second or first != third or second != third:
        print(f'Кол-во равных друг другу чисел - 0')
equals()
