class Animal:
    def __init__(self, name, alive = True, fed = False):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        

class Predator(Animal):
    def eat(self, food):

class Plant:
    def __init__(self,name, edible = False):

class Flower(Plant):
    def __init__(self, edible=False):

class Fruit(Plant):
    def __init__(self, edible=True):


        a1 = Predator('Волк с Уолл-Стрит')
        a2 = Mammal('Хатико')
        p1 = Flower('Цветик семицветик')
        p2 = Fruit('Заводной апельсин')

        print(a1.name)
        print(p1.name)

        print(a1.alive)
        print(a2.fed)
        a1.eat(p1)
        a2.eat(p2)
        print(a1.alive)
        print(a2.fed)
