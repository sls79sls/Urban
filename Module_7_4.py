class result:
    def __init__(self, *args):
        self.args = args
        # print ('type args = ', type(args))

    def old_(self):
        print("В команде Мастера кода участников: %s ! " % team1_num)
        print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

    def for_mat(self):
        print("Команда Волшебники данных решила задач: {} !".format(score_2))
        print("Волшебники данных решили задачи за {} с !".format(team1_time))

    def f_str(self):
        print(f'Команды решили {score_1} и {score_2} задач.')

        if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
            print(f'Победа команды Мастера кода!')
        elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
            print(f'{challenge_result}')
        else:
            print(f'Ничья!')
        print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по '
              f'{round((team1_time + team2_time) / (score_1 + score_2), 1)} секунды на задачу!')


if __name__ == '__main__':
    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    tasks_total = 82
    time_avg = 45.2
    challenge_result = 'Победа команды Волшебники данных!'

    R = result(team1_num, team2_num, score_1, score_2, team1_time, team1_time, tasks_total, time_avg, challenge_result)
    R.old_()
    R.for_mat()
    R.f_str()
