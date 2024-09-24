import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hi, I'm a bot!")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("This bot can execute the commands:\n /start\n /help")

@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answer = random.choice(list)
    await message.answer(rand_answer)

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://funny.klev.club/uploads/posts/2024-03/funny-klev-club-p-smeshnie-kartinki-detskie-dlya-podnyatiya-13.jpg',
            'https://funny.klev.club/uploads/posts/2024-03/funny-klev-club-p-smeshnie-kartinki-detskie-dlya-podnyatiya-12.jpg',
            'https://funny.klev.club/uploads/posts/2024-03/funny-klev-club-p-smeshnie-kartinki-detskie-dlya-podnyatiya-7.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Cool picture!')

if __name__ == "__main__":
    asyncio.run(main())
