import threading
import time

class Knight(threading.Thread):
    def __init__(self,name : str, power : int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        count = 0
        print (f'{self.name}, на нас напали!')
        for i in range(100,0,-(self.power)):
            time.sleep(1)
            count +=1
            print(f'{self.name}, сражается {count} дней, осталось {i-self.power} воинов')
        print(f'{self.name}, одержал победу спустя {count} дней')

if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    thread1 = first_knight
    thread2 = second_knight
    thread1.start()
    # thread1.join()
    thread2.start()
