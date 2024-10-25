from threading import Thread, Lock
from random import randint
from time import sleep

class Bank:
    def __init__(self,balance=0,lock=Lock()):
        self.balance = balance
        self.lock = lock
        
    def deposit(self):
        for i in range(100):
            money = randint(50,500)
            self.balance += money
            print(f'Пополнение: {money} руб. Баланс: {self.balance} руб')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)
            
    def take(self):
        for i in range(100):
            money = randint(50,500)
            print(f'Запрос на {money}')
            if money <= self.balance:
                self.balance -= money
                print(f'Снятие: {money} руб. Баланс: {self.balance} руб')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)
         

if __name__ == '__main__':
    bk = Bank()

    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance} руб')        