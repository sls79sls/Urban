from math import inf
def divide(first_, second_):
    if (second_ == 0):
        return (f'{first_} / {second_} = {inf}')
    else:
        return (f'{first_} / {second_} = {first_/second_}')


if __name__ == "__main__":
    pass
