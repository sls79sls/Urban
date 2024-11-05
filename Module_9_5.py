class StepValueError(ValueError):
    pass
class Iterator:
    def __init__(self, start, stop, step=1):
        self.pointer = start
        self.start = start
        self.stop = stop
        if step == 0 :
            err = 'Шаг не может быть равен нулю'
            print(err)
            raise StepValueError()
        else:
            self.step = step
        print(f'self.pointer={self.pointer} : self.start={self.start} : self.stop={self.stop} : self.step={self.step}')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        #if (self.pointer>1):
        if self.pointer > self.stop:
            raise StopIteration()
        print(f'self.pointer={self.pointer}')
        return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
    print()
for i in iter3:
    print(i, end=' ')
    print()
for i in iter4:
    print(i, end=' ')
    print()
for i in iter5:
    print(i, end=' ')
    print()
