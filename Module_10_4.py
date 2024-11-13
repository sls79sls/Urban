import time
import threading
from queue import Queue
from random import randint

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print (f'len(guests) = {(len(guests))}')
        for i in range(len(guests)):
            self.waiting_ = randint(3, 10)
            print(f'self.name = {self.name}, waiting_ = {self.waiting_}')
            time.sleep(self.waiting_)
            print(f'guests[{i}] = {guests[i]}')
        return self.waiting_

class Cafe(Table, Guest):
    # def __init__(self):
    q = Queue()
    def guest_arrival(self,guests):
        pass

    def discuss_guests(self):

        pass
if __name__ == '__main__':
    tables = [Table(number) for number in range(1, 6)]
    print (f'Table = {list(tables)[0]}')
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
    guests = [Guest(name) for name in guests_names]
    print(f'guests = {guests}')
    #thread = Guest('thread Guests')
    print(f'list guests = {list((guests))}')
    #thread.start()
    cafe = Cafe(tables)
