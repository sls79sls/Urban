class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if (new_floor <= self.number_of_floors):
            for i in range(new_floor):
                print(i + 1)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return (self.number_of_floors)

    def __str__(self):
        return (f'Название: {self.name}, Количество этажей: {self.number_of_floors}')

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self,other):
        return House(self.name, self.number_of_floors + other)

    def __radd__(self,other):
        return self.__add__(other)

    def __iadd__(self,other):
        return self.__add__(other)

if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)
    print(h1)
    print(h2)
    print(h1 == h2)
    h1 = h1 + 10
    print(h1)
    h1 += 10
    print(h1)
    h2 = 10 + h2
    print(h2)
    print(h1 > h2)
    print(h1 >= h2)
    print(h1 < h2)
    print(h1 <= h2)
    print(h1 != h2)
