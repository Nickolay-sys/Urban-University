class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        self.data[username] = password
class User:
    """
    Класс пользователя, соодержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password
    
if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Дратути! Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Подтвердите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден')
        if choice == 2:
            user = User(input('Введите логин: '),
                        password := input('Введите пароль: '),
                        password2 := input('Подтвердите пароль: ')
                        )
            if password != password2:
                continue
            database.add_user(user.username, user.password)
        print(database.data)