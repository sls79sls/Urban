first = 'Мама мыла раму'
second = 'Рамена мало было'
print(len(first))
print(len(second))
result = []
first_list = list(first)
second_list = list(second)
for i in range(len(first),len(second)-1):
    print(f'second[{i}] = {second[i]}')
    first_list[i].append('%')
    print(f'second[{i}] = {second[i]}')
    print(f'first[{i}] = {first[i]}')
for i in range(len(second)):
        print (f'i = {i}')
        print(f'range(len(second) = {range(len(second))}')
        print(f'first[{i}] = {first[i]}')
        print(f'second[{i}] = {second[i]}')
        result = list(map(lambda x, y: x[i] == y[i], first_list, second_list))

