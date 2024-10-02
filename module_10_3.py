from random import randrange
import threading
from time import sleep

class Bank(threading.Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()
        self.transaction = threading.Lock()

    def deposit(self):
        for i in range(500):
            with self.transaction:
                rand = randrange(50,500)
                self.balance += rand
                print(f"Пополнение: {rand}. Баланс: {self.balance}")
                if self.lock.locked() and self.balance >= 500:
                    self.lock.release()
            sleep(0.01)


    def take(self):
        for i in range(500):
            with self.transaction:
                rand = randrange(50,500)
                if rand > self.balance:
                    print('Запрос отклонён, недостаточно средств')
                    if not self.lock.locked():
                        self.lock.acquire()
                else:
                    self.balance -= rand
                    print(f"Снятие: {rand}. Баланс: {self.balance}")
            sleep(0.01)
                # self.lock.release()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print("end")