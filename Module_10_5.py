import multiprocessing as mp
import datetime

def read_info(name):
    all_data = []
    file = open(name, "r")
    while True:
        line = file.readline()
        all_data.append(line)
        if not line:
            break
        #print(line.strip())
    file.close
    return (all_data)

if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]
    start = datetime.datetime.now()
    read_info(filenames[0])
    read_info(filenames[1])
    read_info(filenames[2])
    read_info(filenames[3])
    end = datetime.datetime.now()
    print(f'Monoprocessing : {end - start} секунд')

    pool = Pool([4, read_info(), filenames[0], maxtasksperchild
                 [, context])
