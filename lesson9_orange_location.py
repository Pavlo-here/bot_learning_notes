# practice on bot keyboard sending orange pic and random location
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API
from random import random


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("/help")
b2 = KeyboardButton("/orange")
b3 = KeyboardButton("/location")
b4 = KeyboardButton("/close_keyboard")
kb.add(b1).insert(b2).insert(b3).add(b4)

HELP_COMMAND = """
<b>/help</b> - <em>допомога</em>
<b>/start</b> - <em>старт бота</em>
<b>/orange</b> - <em>відправка фото апельсина у чат</em>
<b>/location</b> - <em>відправка випадкової геолокації</em>
"""


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, text="Starting bot...", reply_markup=kb)


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(message.chat.id, text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=["close_keyboard"])
async def close_keyboard(message: types.Message):  # close keyboard button
    await bot.send_message(message.chat.id, text="Keyboard removed!", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands="orange")
async def heart(message: types.Message):  # send photo of orange
    await bot.send_photo(message.chat.id, photo="https://upload.wikimedia.org/wikipedia/commons/thumb"
                                                "/e/e3/Oranges_-_whole-halved-segment.jpg/640px-Oranges"
                                                "_-_whole-halved-segment.jpg")


@dp.message_handler(commands=["location"])
async def random_location(message: types.Message):  # send random location
    await bot.send_location(chat_id=message.chat.id, latitude=random()*100, longitude=random()*100)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
