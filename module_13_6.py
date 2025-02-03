from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands = 'start')
async def start_message(message):
    await message.answer("Привет, для выбора команд, используй, пожалуйста клавиатуру, справа от командной строки ",
                         reply_markup = keyboard)

@dp.message_handler(text = "Информация")
async def set_age(message):
    await message.answer ("Информация о БОТе")

@dp.message_handler(text = "Рассчитать")
async def inl_kb(message):
    await message.answer("Пожалуйста, выберите опцию:", reply_markup = kbi)

@dp.callback_query_handler(text='info')
async def inform(call):
    await call.message.answer("weight*10 + 6.25*growth - 5*age - 161")
    await call.answer()

@dp.callback_query_handler(text='calc')
async def set_age(call):
    await call.message.answer ("Пожалуйста, введите свой возраст:")
    await call.answer()
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
    await message.answer(f"Ваша норма калорий: {Calories}", reply_markup=types.ReplyKeyboardRemove(True))
    #await message.reply("Отличный выбор!") Отвечает на последнее сообщение
    await state.finish()

@dp.message_handler()
async def all_message(message):
    print(f"Принято какое то сообщение - {message.text} Рекомендовано запустить команду  /start")
    await message.answer("Для начала работы с ботом , введите пожалуйста команду /start")

if __name__ == '__main__':
    kb = [
        [
            types.KeyboardButton(text="Рассчитать"),
            types.KeyboardButton(text="Информация")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    kbi = InlineKeyboardMarkup()
    buttoni1 = InlineKeyboardButton(text="Формулы расчёта", callback_data='info')
    buttoni2 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calc')
    kbi.add(buttoni1)
    kbi.add(buttoni2)
    executor.start_polling(dp,skip_updates=True)
