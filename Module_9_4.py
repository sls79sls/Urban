first = 'Мама мыла раму'
second = 'Рамена мало было'
print(type(first))
print(list(first))
print(type(first))
for i in range(len(second)):
    print (f'i = {i}')
    print(f'range(len(second) = {range(len(second))}')
    print(f'first[{i}] = {first[i]}')
    print(f'second[{i}] = {second[i]}')
    list(map(lambda x, y: list(x[i]) == list(y[i]), first, second))
