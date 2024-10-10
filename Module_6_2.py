class Vehicle:

    COLOR_VARIANTS = ['WHITE', "BLUE", "RED", "BLACK"]
    def __init__(self, owner : str, __model : str, __color : str, __engine_power : int):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    def get_model(self):
        print ("Модель : ",self.__model)
    def horcepower(self):
        print("Мощность двигателя : ", self.__engine_power)
    def get_color(self):
        print("Цвет : ", self.__color)
    def print_info(self):
        self.get_model()
        self.horcepower()
        self.get_color()
        print("Владелец : ", self.owner)
    def set_color(self,new_color):
        if new_color.lower() != self.__color.lower():
            for i in range(len(self.COLOR_VARIANTS)):
                if self.COLOR_VARIANTS[i].lower() == new_color.lower():
                    self.__color = new_color
                else:
                    if (self.__color != new_color and (i+1) >= len(self.COLOR_VARIANTS)):
                        print(f"Нельзя сменить цвет на {new_color}")
        else:
            print(f"Красим авто в тот же цвет : {self.__color}")



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.set_color('BLUE')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
