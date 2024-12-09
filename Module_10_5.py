import multiprocessing as mp
from multiprocessing import Pool
import datetime


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        while True:
            line = file.readline()
            all_data.append(line.strip())
            if not line:
                break
    return all_data


if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    start = datetime.datetime.now()
    for file in filenames:
        read_info(file)
    end = datetime.datetime.now()
    print(f'Monoprocessing : {end - start} секунд')

    start_pool = datetime.datetime.now()
    with Pool(3) as pool:
        pool.map(read_info, filenames)
    end_pool = datetime.datetime.now()
    print(f'Multiprocessing : {end_pool - start_pool} секунд')
