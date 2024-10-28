class Func:
    def __init__(self,*args):
        self.args = args

    def personal_sum(self,numbers):
        global sum_, incorrect_data
        incorrect_data = 0
        sum_ = 0
        try:
            for i in numbers:
                try:
                    sum_ = sum_ + i
                except TypeError:
                    incorrect_data += 1
                    print(f'Некорректный тип данных для подсчёта суммы - {i}')

        except TypeError:
            pass
        return sum_, incorrect_data

    def calculate_average(self, numbers):
        global avg
        x = self.personal_sum(numbers)
        try:
            avg = x[0]/(len(numbers)-x[1])
        except ZeroDivisionError:
            avg = 0
        except TypeError:
            print('В numbers записан некорректный тип данных')
            avg = None
        return avg

if __name__ == '__main__':
    F = Func()
    F.calculate_average("1, 2, 3")
    print(f'Результат 1: {avg}')
    F.calculate_average([1, "Строка", 3, "Ещё Строка"])
    print((f'Результат 2: {avg}'))
    F.calculate_average(567)
    print((f'Результат 3: {avg}'))
    F.calculate_average([42, 15, 36, 13])
    print ((f'Результат 4: {avg}'))
