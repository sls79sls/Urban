import time
import threading
from queue import Queue
from random import randint

class Table:
    def __init__(self, *number):
        self.number = number
        self.guest = None
    def __str__(self):
        return f'{self.number}'

if __name__ == '__main__':
    tables = [Table(number) for number in range(1, 6)]
    for i in range(len(list(tables))):
        print (f'tables[{i}] = {(tables[i].number)}')
    print (f'list(tables) = {list(tables)}')
    print (tables)
