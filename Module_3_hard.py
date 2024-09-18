def kortej(var_):
    global sum_
    for k in range(len(var_)):
        if var_[k] == ():
            continue
        if (isinstance(var_[k], list)):
            spisok(var_[k])
            data_structure.pop(0)
            calculate_structure_sum(data_structure)
        if (isinstance(var_[k], int)):
            sum_ = sum_ + int(var_[k])
        if (isinstance(var_[k], dict)):
            slovar(var_[k])
        if (isinstance(var_[k], str)):
            sum_ = sum_ + len(var_[k])
        if (isinstance(var_[k], tuple)):
            for m in var_[k]:
                if (isinstance(m, int)):
                    sum_ = sum_ + m
                if (isinstance(m, str)):
                    sum_ = sum_ + len((m))
    return sum_


def spisok(var_):
    global sum_
    for i in range(len(var_)):
        if (isinstance(var_[i], int)):
            sum_ = sum_ + int(var_[i])
        else:
            if (isinstance(var_[i], str)):
                sum_ = sum_ + len(var_[i])
            if (isinstance(var_[i], set)):
                invar_ = var_[i]
                for n in invar_:
                    if (isinstance(n, tuple)):
                        kortej(n)
                    if (isinstance(n, str)):
                        sum_ = sum_ + len(n)
                    if (isinstance(n, list)):
                        spisok(n)

    return sum_


def slovar(var_):
    global sum_
    for key_, value_ in var_.items():
        if (isinstance(key_, int)):
            sum_ = sum_ + int(key_)
        if (isinstance(key_, str)):
            sum_ = sum_ + len((key_))
        if (isinstance(value_, int)):
            sum_ = sum_ + int(value_)
        if (isinstance(value_, str)):
            sum_ = sum_ + len((value_))
    return sum_


def calculate_structure_sum(data_structure):
    global sum_

    if data_structure == []:
        return sum_
    else:
        var_ = data_structure[0]
        if (isinstance(var_, list)):
            spisok(var_)
            data_structure.pop(0)
            calculate_structure_sum(data_structure)
        if (isinstance(var_, tuple)):
            kortej(var_)

            if data_structure != []:
                data_structure.pop(0)
                calculate_structure_sum(data_structure)
            return sum_

        if (isinstance(var_, dict)):
            slovar(var_)
            data_structure.pop(0)
            calculate_structure_sum(data_structure)

        if (isinstance(var_, str)):
            sum_ = sum_ + len(var_)
            data_structure.pop(0)
            calculate_structure_sum(data_structure)
            return sum_
    return sum_


if __name__ == "__main__":
    sum_ = 0
    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
    result = calculate_structure_sum(data_structure)
    print('result = ', result)
