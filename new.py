import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.storage.memory import MemoryStorage
import aiohttp
import sqlite3
import logging
from config import TOKEN, WEATHER_API_KEY


bot = Bot(token=TOKEN)
dp = Dispatcher()

url_weather = 'http://api.openweathermap.org/data/2.5/weather'
logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    name = State()
    age = State()
    city = State()

def init_db():
    conn = sqlite3.connect('user_data.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        city TEXT NOT NULL)
    ''')
    conn.commit()
    conn.close()

init_db()

@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Hi! What is your name?")
    await state.set_state(Form.name)

@dp.message(Form.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("How old are your?")
    await state.set_state(Form.age)

@dp.message(Form.age)
async def age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("What city are you from?")
    await state.set_state(Form.city)

@dp.message(Form.city)
async def city(message: Message, state:FSMContext):
    await state.update_data(city=message.text)
    user_data = await state.get_data()

    conn = sqlite3.connect('user_data.db')
    cur = conn.cursor()
    cur.execute('''
       INSERT INTO users (name, age, city) VALUES (?, ?, ?)''',
                (user_data['name'], user_data['age'], user_data['city']))
    conn.commit()
    conn.close()

    # finalize state and clear data
    # await state.finish()
    await state.clear()

    # Sending a message to the user about the completion of a process
    # await message.reply("Your data has been saved successfully!")

    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{url_weather}?q={user_data['city']}&appid={WEATHER_API_KEY}&units=metric") as response:
            if response.status == 200:
                weather_data = await response.json()
                main_block = weather_data['main']
                weather = weather_data['weather'][0]
                temperature = main_block['temp']
                humidity = main_block['humidity']
                description = weather['description']

                weather_report = (f"City: {user_data['city']}\n"
                                  f"Temperature: {temperature}\n"
                                  f"Humidity: {humidity}\n"
                                  f"Weather description: {description}")
                await message.answer(weather_report)
            else:
                await message.answer("Unable to retrieve weather data")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
