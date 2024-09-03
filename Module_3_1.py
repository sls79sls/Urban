calls = 0
def count_calls():
    global calls
    calls = calls + 1


def string_info(string_):
    tuple_string = (len(string_),string_.upper(),string_.lower())
    count_calls()
    return(tuple_string)


def is_contains(string_,list_to_search):
    for i in list_to_search:
        if str(i.lower()) == str(string_.lower()):
            answer_ = True
            break
        else:
            answer_ = False
    count_calls()
    return (answer_)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(is_contains('Fider', ['Fiberglass', 'Fider', 'Final']))
print(calls)
