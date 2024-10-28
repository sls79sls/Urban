class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model :str, __vin : int, __number : str):
        self.model = model
        self.__vin = __vin
        self.__number = __number
        self.__is_valid_vin(__vin)

    @property
    def vin(self):
        return self.__vin
    @vin.setter
    def vin(self, val):
        self.__vin = val

    def __is_valid_vin(self,vin_number):
        #vin_number = self.__vin
        print(f'vin_number = {vin_number}')
        if (isinstance (vin_number, int) and 1000000 <= vin_number <= 9999999):
            check_ = True
        else:
            check_ = False
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return check_
    
if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as err:
        print(f"{err.message}")
    print(first.__is_valid_vin.check_)
