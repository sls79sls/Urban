import threading
from random import randint
import time
counter = 0

class Bank():
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()
        print(f'на старт , внимание, марш')
        print (f'lock = {self.lock.locked()} , balance = {self.balance}')

    def deposit(self):
        if (self.lock.locked() and self.balance>=500):
            self.lock.release()
        for i in range(100):
            x = randint(50,500)
            self.balance += x
            time.sleep(0.001)
            print (f'Пополнение {i}-е на: {x} . Баланс : {self.balance}')
            if (self.lock.locked() and self.balance >= 500):
                self.lock.release()
    def take(self):

        for i in range(100):
            x = randint(50,500)
            print(f'Запрос {i}-й на : {x}')
            if (not(self.lock.locked()) and self.balance >= x):
                print(f'Снятие : {x}, ,Баланс : {self.balance}')
                self.balance -= x
                time.sleep(0.001)
            elif ((self.lock.locked() and self.balance < x) or self.balance < x):
                print (f'Lock = {self.lock.locked()} , balance = {self.balance}')
                print (f'Запрос {i} отклонён, недостаточно средств')
                self.lock.acquire()


if __name__ == '__main__':
    bk = Bank()
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(f'Итоговый баланс: {bk.balance}')
