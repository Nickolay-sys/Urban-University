"""
try - проверяет написаные в ней блоки с возможной ошибкой
exept - выполняет написаные в ней блоки кода в случае возникновения ошибки в блоке try
else - вызывается если небыло ошибок в блоке try
finally - выполняется всегда

В блоке expet лучше указывать класс ошибки, если он известен
У этих блоков есть возможность сохранить название ошибки в переменую и вывести её в консоль
"""
i = int(input('Enter your number: '))
try:
    result = 10 * (1/i)   
except ZeroDivisionError as exc:
    print(f'Dont divide by zero! {exc}')
except NameError:
    print("There no such variable")
else:
    print(f'You didnt divide by zero! Congrats!')
    print(result)
finally:
    print('Finally lection is over :)')
       