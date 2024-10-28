class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model :str, __vin : int, __number : str):
        self.model = model
        self.__vin = __vin
        self.__number = __number
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__number)

    @property
    def vin(self):
        return self.__vin
    @vin.setter
    def vin(self, val):
        self.__vin = val

    def __is_valid_vin(self,vin_number):
        if (isinstance (vin_number, int) and 1000000 <= vin_number <= 9999999):
            check_ = True
        else:
            check_ = False
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return check_

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val):
        self.__number = val

    def __is_valid_numbers(self, number):
        if isinstance (number, str):
            check_ = True
        else:
            check_ = False
            raise IncorrectCarNumber('Некорректный тип данных для номеров')

        if (len(number) != 6):
            check_ = False
            raise IncorrectCarNumber('Неверная длина номера')
        else:
            check_ = True
        return check_

if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as err:
        print(f"{err.message}")
    except IncorrectCarNumber as err:
        print(f"{err.message}")
    else:
        print(f'{first.model} - Успешно создан')

    try:
        second = Car('Model2', 300, '1т001тр')
    except IncorrectVinNumber as err:
        print(f"{err.message}")
    except IncorrectCarNumber as err:
        print(f"{err.message}")
    else:
        print(f'{second.model} - Успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as err:
        print(f"{err.message}")
    except IncorrectCarNumber as err:
        print(f"{err.message}")
    else:
        print(f'{third.model} - Успешно создан')
