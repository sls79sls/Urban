def is_prime(func):
    def wrapper(*args):
        uns = func(*args)
        for i in range(2,int(uns)-1):
            if (not(uns % i)):
                answ = 'Не простое'
                break
            else:
                answ = 'Простое'
        return answ
    return wrapper

@is_prime
def sum_three(*args):
    sum_ = 0
    for i in args:
        sum_ += int(i)
    print (f'sum_ = {sum_}')
    return sum_

if __name__ == '__main__':

    print(sum_three(2, 3, 6))


