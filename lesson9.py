# practice on bot keyboard
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("/help")
b2 = KeyboardButton("/description")
b3 = KeyboardButton("❤️")
b4 = KeyboardButton("/close_keyboard")
kb.add(b1).insert(b2).insert(b3).add(b4)

HELP_COMMAND = """
<b>/help</b> - <em>допомога</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>опис функціоналу бота</em>
"""


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text="Starting bot...", reply_markup=kb)


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=["description"])
async def description_command(message: types.Message):
    await bot.send_message(message.from_user.id, text="Here is description of bot", parse_mode="HTML")


@dp.message_handler(commands=["close_keyboard"])
async def close_keyboard(message: types.Message):
    await bot.send_message(message.from_user.id, text="Keyboard removed!", reply_markup=ReplyKeyboardRemove())


@dp.message_handler()
async def heart(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAAEJbvJklASnBym5mF2sbsg-GzQRpT5FlwACdwADhIUKFrFQQrqaZrbXLwQ")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
