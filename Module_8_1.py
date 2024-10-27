class Summa:
    def __init__(self, *args):
        self.args = args

    def add_everything_up(self,a,b):
        try:
            print (f'{a} + {b} = {(a+b):.3f}')
        except TypeError:
            print(f'{a}{b}')

if __name__ == '__main__':
    
    S = Summa()
    S.add_everything_up(123.456, 'строка')
    S.add_everything_up('яблоко', 4215)
    S.add_everything_up(123.456, 7)
