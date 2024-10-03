import queue
from random import randrange
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        sleep(randrange(3,10))

class Cafe:
    def __init__(self,*args):
        for i in args:
            if not isinstance(i,Table):
                raise TypeError
        self.queue = queue.Queue()
        self.tables = args
    def guest_arrival(self, *guests):
        for i in guests:
            if not isinstance(i,Guest):
                raise TypeError
        j = 0
        for i in guests:
            if j == len(self.tables)-1:
                self.queue.put(i)
                print(f"{i.name} в очереди")
                continue

            for k in range(j,len(self.tables)):
                if self.tables[k].guest is None:
                    self.tables[k].guest = i
                    i.start()
                    j = k
                    print(f"{i.name} сел(-а) за стол номер {self.tables[k].number}")
                    break





    def discuss_guests(self):
        unpoisoned = True
        def disposer(table):
            print(f'{table.guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {table.number} свободен')
            table.guest = None
        def check_queue(table):
            if not self.queue.empty():
                table.guest = self.queue.get()
                print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                return True
            return False
        while unpoisoned:
            unpoisoned = False
            for i in self.tables:
                if i.guest is not None:
                    if i.guest.is_alive():
                        unpoisoned = True
                        continue
                    else:
                        disposer(i)
                        if check_queue(i):
                            unpoisoned = True
                            i.guest.start()
                            continue


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