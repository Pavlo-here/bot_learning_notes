# work with keyboard
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)  # !
b1 = KeyboardButton('/help')  # button 1
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/photo')
kb.add(b1).insert(b2).add(b3)

HELP_COMMAND = """
<b>/help</b> - <em>допомога</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>опис функціоналу бота</em>
<b>/photo</b> - <em>відправити фото</em>
"""


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Вітаємо у нашому боті!", parse_mode="HTML",
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=["description"])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Ми відправляємо фото", parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=["photo"])
async def photo_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://lh3.googleusercontent.com/p/AF1QipNJ_gwYUdNHhUB_ESDYIB605SaowpaM2nmJwY2i=s680"
                               "-w680-h510")
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
