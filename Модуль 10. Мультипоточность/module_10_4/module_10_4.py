from threading import Thread
from time import sleep
from random import randint
from queue import Queue

class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
        
    def run(self):
        sleep(randint(3,10))


                
class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()
    
    def guest_arrival(self,*guests):
        served = []
        for g in guests:
            for t in self.tables:
                if t.guest == None:
                    served.append(g)
                    t.guest = g
                    print(f'{g.name} сел(-а) за стол номер {t.number}')
                    break
            if (g in served) == False:
                self.queue.put(g)
                print(f'{g.name} в очереди')
        for g in served: g.start() 
            
    def discuss_guests(self):
        free_tables = 0
        while True:
            for t in self.tables:
                if (t.guest.is_alive() == False) or (self.queue.empty()):
                    print(f'{t.guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {t.number} свободен')
                    t.guest.join()
                    t.guest = None
                if (self.queue.empty() == False) and (t.guest == None):
                    t.guest = self.queue.get()
                    print(f'{t.guest.name} вышел(-ла) из очереди и сел(-ла) за стол номер {t.number}')
                    t.guest.start()
                elif t.guest == None:
                    free_tables += 1
                    if free_tables == len(self.tables):
                        return

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()