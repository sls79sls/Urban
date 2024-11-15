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
        self.waiting_ = randint(0, 2)
        time.sleep(self.waiting_)
        return self.waiting_

class Cafe(Table, Guest):
    global guests
    def __init__(self,*tables):
        threading.Thread.__init__(self)
        self.guests = guests
    q = Queue()
    q.put(self.guests)
    print (f'q.get(guests) = {q.get(guests)}')
    def guest_arrival(self,*guests):
        global count_
        print(f'len(list(*guests)) : {len(list(*guests))}')
        print(f'len(list(tables)) : {len(list(tables))}')
        while (count_ <= len(list(*guests))):
            for i in range (1,len(list(tables))):
                print(f'i =  : {i}')
                if (tables[i].guest == None):
                    tables[i].guest = guests[count_]
                    thread = Guest('thread Guests')
                    thread.start()
                    print(f'Гость, {self.guests[count_]}, сел за стол {i}')
                continue
            count_ += 1
            print(f'self.guests[count_] : {self.guests[count_]}')
    def discuss_guests(self):
        pass
if __name__ == '__main__':
    count_ = 0
    tables = [Table(number) for number in range(1, 6)]
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
    guests = [Guest(name) for name in guests_names]
    #thread = Guest('thread Guests')
    #thread.start()
    cafe = Cafe(*tables)
    cafe.guest_arrival(guests)
    cafe.discuss_guests()
