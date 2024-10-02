import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
import random
from config import TOKEN
from gtts import gTTS
import os

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

@dp.message(Command('video'))
async def video(message: Message):
    video_file = FSInputFile('tmp/video1.mp4')
    await bot.send_video(message.chat.id, video_file)
    await bot.send_chat_action(message.chat.id, 'upload_video')

@dp.message(Command('audio'))
async def audio(message: Message):
    audio_file = FSInputFile('tmp/sound2.m4a')
    # await bot.send_audio(message.chat.id, audio_file)
    await message.answer_audio(audio_file, "Cool audio!")

@dp.message(Command('training'))
async def training(message: Message):
   training_list = [
       "Тренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
       "Тренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
       "Тренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
   ]
   rand_tr = random.choice(training_list)
   await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")
   tts = gTTS(text=rand_tr, lang='en')
   tts.save("tmp/training.mp3")
   audio_file = FSInputFile('tmp/training.mp3')
   await bot.send_audio(message.chat.id, audio_file)
   os.remove("tmp/training.mp3")

@dp.message(Command('voice'))
async def voice(message: Message):
    voice_file = FSInputFile("tmp/sample3.ogg")
    await message.answer_voice(voice_file)

@dp.message(Command('doc'))
async def doc(message: Message):
    doc_file = FSInputFile("tmp/sol.pdf")
    await bot.send_document(message.chat.id, doc_file)

@dp.message()
async def start(message: Message):
    if message.text.lower() == 'test':
        await message.answer('Testing')
    else:
        await message.answer("Sorry, I didn't understand that command or message. Please try again.")


'''
# echo-bot
@dp.message()
async def start(message: Message):
    await message.send_copy(chat_id=message.chat.id)
'''


if __name__ == "__main__":
    asyncio.run(main())
