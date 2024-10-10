class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        print(f"self.food = {self.food}")
        if self.food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')


class Mammal(Animal):
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed
        self.eat


class Predator(Animal):
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed
        self.eat

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible


class Flower(Plant):
    def __init__(self, name, edible=True):
        self.edible = edible
        self.name = name


class Fruit(Plant):
    def __init__(self, name, edible=True):
        self.edible = edible
        self.name = name

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)



print(f"a1.alive = {a1.alive}")
print(f"a2.fed = {a2.fed}")
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
