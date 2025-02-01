from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
@dp.message_handler(text = "Calories")
async def set_age(message):
    await message.answer ("Пожалуйста, введите свой возраст:")
    await UserState.age.set() # Состояние для которого пишется нижеследующий Handler

@dp.message_handler(state = UserState.age)
async def fcm_set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer("Пожалуйста, введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def fcm_set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer("Пожалуйста, введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def fcm_send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    print(f"data[age] = {data['age']}")
    print(f"data[growth] = {data['growth']}")
    print(f"data[weight] = {data['weight']}")
    Calories = int (data['weight'])*10+6.25*int (data['growth'])-5*int(data['age'])-161
    print(f"Calories = {Calories}")
    await message.answer(f"Ваша норма калорий: {Calories}")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
