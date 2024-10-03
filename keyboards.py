from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Test button 11")],
   [KeyboardButton(text="Test button 21"), KeyboardButton(text="Test button 22")]
], resize_keyboard=True)

# inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
#    [InlineKeyboardButton(text="Video", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk')]
# #   [InlineKeyboardButton(text="Github", url='https://github.com/aiogram/aiogram')]
# ])

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Catalog", callback_data='catalog')],
   [InlineKeyboardButton(text="News", callback_data='news')],
   [InlineKeyboardButton(text="Person", callback_data='person')]
])

test = ["but 1", "but 2", "but 3", "but 4"]

async def test_keyboard():
   keyboard = ReplyKeyboardBuilder()
   for key in test:
       keyboard.add(KeyboardButton(text=key))
   return keyboard.adjust(2).as_markup()


async def test_inline_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test:
       keyboard.add(InlineKeyboardButton(text=key, url='https://github.com/aiogram/aiogram'))
   return keyboard.adjust(2).as_markup()