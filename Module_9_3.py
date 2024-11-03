first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(list(zip(first,second))[i][0]) - len(list(zip(first,second))[i][1]) for i in range(len(first))
                if len(list(zip(first,second))[i][0]) != len(list(zip(first,second))[i][1])]

second_result = list(map(lambda x, y : len(x) == len(y) , first , second))

print (list(first_result))
print (list(second_result))
