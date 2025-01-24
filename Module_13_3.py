from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7613891082:AAHK3Y2o_A5QWhvZZbUgeV-JG0zQoKZIMEs"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(text = ["Urban", "FF"])
async def urban_message(message):
    print("Urban message")
    await message.answer("Urban message")

@dp.message_handler(commands = ['start'])
async def start_message(message):
    print("Введена команда \start")
    await message.answer("Привет, я БОТ, помогающий твоему здоровью")

@dp.message_handler(text = ['Привет' , 'привет' , 'Hi' , 'Hello' , 'Здравствуйте'])
async def all_message(message):
    print("Принято соощение типа  \ПРИВЕТ\. Рекомендовано запустить команду \start")
    await message.answer("Для начала работы с ботом , введите пожалуйста команду \start")

@dp.message_handler()
async def all_message(message):
    print("Принято какое то сообщение. Рекомендовано запустить команду  \start")
    await message.answer("#Для начала работы с ботом , введите пожалуйста команду \start")

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)



