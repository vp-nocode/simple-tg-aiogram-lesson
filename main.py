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
    await message.answer(f"Hi, {message.from_user.first_name} ({message.from_user.full_name}), I'm a bot!")

@dp.message(Command('help'))
async def command_help(message: Message):
    await message.answer("This bot can execute the commands:\n /start\n /help")

@dp.message(F.text == "What is AI?")
async def aitext(message: Message):
    await message.answer('Artificial intelligence is the ability of artificial intelligent systems to perform creative'
                         ' functions traditionally considered the prerogative of humans; the science and technology '
                         'of creating intelligent machines, especially intelligent computer programs ')

@dp.message(F.photo)
async def react_photo(message: Message):
    message_list = ['Wow, what a photo!', 'I don\'t understand what this is', 'Don\'t send me that again']
    rand_answer = random.choice(message_list)
    await message.answer(rand_answer)
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')

@dp.message(Command('photo', prefix='&'))
async def photo(message: Message):
    photo_list = ['https://funny.klev.club/uploads/posts/2024-03/funny-klev-club-p-smeshnie-kartinki-detskie-dlya-podnyatiya-13.jpg',
            'https://funny.klev.club/uploads/posts/2024-03/funny-klev-club-p-smeshnie-kartinki-detskie-dlya-podnyatiya-12.jpg',
            'https://funny.klev.club/uploads/posts/2024-03/funny-klev-club-p-smeshnie-kartinki-detskie-dlya-podnyatiya-7.jpg']
    rand_photo = random.choice(photo_list)
    await message.answer_photo(photo=rand_photo, caption='Cool picture!')

@dp.message()
async def start(message: Message):
    if message.text.lower() == 'test':
        await message.answer('Testing')

@dp.message()
async def start(message: Message):
    await message.answer("Sorry, I didn't understand that command or message. Please try again.")

'''
# echo-bot
@dp.message()
async def start(message: Message):
    await message.send_copy(chat_id=message.chat.id)
'''


if __name__ == "__main__":
    asyncio.run(main())
