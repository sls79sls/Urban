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
        self.waiting_ = randint(3, 10)
        time.sleep(self.waiting_)

class Cafe:
    def __init__(self,*tables):
        self.tables = tables
        self.q = Queue()
    def guest_arrival(self, *guests):
        #global guest
        for guest in guests:
            free_table = None
            for table in self.tables:
                if table.guest == None:
                    free_table = table
                    break
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.q.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        #global guest
        while (not self.q.empty()):
            #print (f'self.q.empty() = {self.q.empty()}')
            for table in self.tables:
                #print(f'table.guest = {table.guest}')
                if table.guest:
                    if (not table.guest.is_alive()):
                        #print(f'table.guest.name = {table.guest.name}')
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла), Стол номер {table.number} свободен")
                        table.guest = None
                        if (not self.q.empty()):
                            table.guest = self.q.get()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            table.guest.start()
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
    cafe.guest_arrival(*guests)
    cafe.discuss_guests()
