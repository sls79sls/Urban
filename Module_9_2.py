first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
third_strings = []
first_result = [len(i) for i in first_strings if len(i)>=5]
second_result = [(f_list,s_list) for f_list in first_strings for s_list in second_strings
                 if(len(f_list) == len(s_list))]
for i in first_strings:
    third_strings.append(i)
for i in second_strings:
    third_strings.append(i)

third_result = [(i, len(i)) for i in third_strings if not (len(i) %2)]

print(f'first_result = {first_result}')
print(f'second_result = {second_result}')
print(f'third_result = {third_result}')
