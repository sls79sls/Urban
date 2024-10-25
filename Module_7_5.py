import os
import time
directory = 'C:\Disk-D\Project_Python_Urban\pythonProject'
os.chdir(directory)
print(os.getcwd())
for i in os.walk ('.'):
    for j in range(len(i[2])):
        if 'Module_5_hard' in i[2][j]:
            print('Файл обнаружен : ', i[2][j])
            break

path_ = os.path.join(directory,'Module_5_hard.py')
print('path = ', path_)
time_ = os.path.getmtime(directory+'\Module_5_hard.py')
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(time_))
print('Path = ', formatted_time , 'sec')
print('Size = ', os.path.getsize(directory+'\Module_5_hard.py'), 'Bytes')
print('Parents catalogue :', os.path.dirname(directory+'\Module_5_hard.py'))
