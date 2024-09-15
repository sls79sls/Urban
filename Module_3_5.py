def get_multiplied_digits(number):
    str_number = str(number)
    print('str_number = ', str_number)
    print('длина str_number = ', len(str_number))
    if len(str_number) >> 1:
        first = int(str_number[0:1])
        print ('first = ', first)
        print('str_number = ',str_number[1:])
        return(first * get_multiplied_digits(int(str_number[1:])))
    elif len(str_number) == 1:
        first = int(str_number[0:1])
        return first

if __name__ == '__main__':
    print('Итог : ',get_multiplied_digits(40203))
