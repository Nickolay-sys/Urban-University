name = input('Введите ваше имя: ')      # команда input() запрашивает ввод через терминал
print(type(name))       # все данные введёные через терминал имеют тип данных строка
current_year = 2024
date_of_birth = input('В каком году вы родились: ')
age = current_year - int(date_of_birth)      # при необходимости нужно изменить тип данных


print(f'Здравтствуйте, {name}')
print(f'В этом году вам {age} лет')
print(f'ПРИВЕТ, Я СТРОКА В НИЖНЕМ РЕГИСТРЕ'.lower())     # метод .lower() переводит строку в нижний регистр
print(f'привет, я строка в верхнем регистре'.upper())        # метод .upper() переводит строку в верхний регистр
print(f'привет, я строка в нижнем регистре'.replace('привет','пока'))        # метод .replace() заменяет первый указанный символ на второй указанный символ
print(f'привет, я строка в нижнем регистре'.replace(' ',''))    
