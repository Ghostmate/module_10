from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        k = 0
        for i in range(100,0,-self.power):
            print(f'{self.name} сражается {k} дней, осталось {i} воинов.')
            sleep(1)
            k += 1
        print(f"{self.name} одержал победу спустя {k} дней(дня)!")



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')