import threading
import time


def write_words(word_count, file_name):
    data = 'Какое-то слово №'
    with open(file_name, "w") as file:
        for i in range(int(word_count)):
            file.write(data)
            file.write(str(i + 1))
            file.write('\n')
            time.sleep(0.1)
        print(f'Запись в файл {file_name} успешно завершена')


if __name__ == '__main__':
    print(threading.enumerate())
    started_at = time.time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    ended_at = time.time()
    print(f'Работа потоков : {ended_at-started_at}')
    print(threading.current_thread())
    started_at = time.time()
    thread = threading.Thread(target=write_words, args=(10, 'example5.txt'))
    thread.start()
    thread = threading.Thread(target=write_words, args=(30, 'example6.txt'))
    thread.start()
    thread = threading.Thread(target=write_words, args=(200, 'example7.txt'))
    thread.start()
    thread = threading.Thread(target=write_words, args=(100, 'example8.txt'))
    thread.start()
    thread.join()
    ended_at = time.time()
    print(f'Работа потоков : {ended_at - started_at}')
