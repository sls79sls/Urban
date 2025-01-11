import time
import asyncio

async def start_strongman(name, power): # 1 - я  Асинхронная функция
    n = 1
    print(f"Силач {name} начал соревнования.")
    while n<=5:
        await asyncio.sleep(1/power)
        print(f"Силач {name} поднял номер шара {n}.")
        n += 1
    print(f"Силач {name} законил соревнования.")

async def start_tournament():
    print ("Старт")
    task1 = asyncio.create_task(start_strongman("Pasha", 3)) # task запускается и программа движется дальше
    task2 = asyncio.create_task(start_strongman("Denis", 4))
    task3 = asyncio.create_task(start_strongman("Apollon", 5))
    await task1 # ДЛЯ ТОГО, ЧТОБЫ ДОЖДАТЬСЯ ЗАВЕРШЕНИЯ РАБОТ ПО ЭТИМ ЗАДАНИЯМ ПИШЕМ ОБЯЗАТЕЛЬНО await
    await task2 # иначезавершения работ не произойдёт, и программа завершит работу,
    await task3
    print("Финиш")

asyncio.run(start_tournament()) # Запуск main() теперь нужно писать таким образом
