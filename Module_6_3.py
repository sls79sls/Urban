class Horse:
    def __init__(self, x_distance = 0, sound = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__()

    def run(self, dx):

        self.x_distance = self.x_distance + dx

    def __add__(self, other):
        return Horse(self.dx + other)

    def __add__(self, other):
        return Horse(self.dy + other)


class Eagle:
    def __init__(self,y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound
        super().__init__()

    def fly(self, dy):
        self.y_distance = self.y_distance + dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()


    def move(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy
        self.run(dx)
        self.fly(dy)
        return self.x_distance, self.y_distance

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print (self.sound)




p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
