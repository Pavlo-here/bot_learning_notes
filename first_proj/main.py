from aiogram import types, Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
import random

from keyboards import kb, kb_photo
from config import TOKEN_API


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)

HELP_TEXT = """
<b>/help</b> - <em>command list</em>
<b>/start</b> - <em>launch bot</em>
<b>/description</b> - <em>bot's description</em>
<b>/random_photo</b> - <em>send random photo</em>
<b>/close</b> - <em>close keyboard</em>
"""

random_photos = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8"
                 "/Altja_j%C3%B5gi_Lahemaal.jpg/1200px-Altja_j%C3%B5gi_Lahemaal.jpg",
                 "https://natureconservancy-h.assetsadobe.com/is/image/content/dam/tnc/nature"
                 "/en/photos/Zugpsitze_mountain.jpg?crop=0%2C214%2C3008%2C1579&wid=1200&hei=630&scl=2.506666666666667",
                 "https://cdn.pixabay.com/photo/2014/02/27/16/10/flowers-276014_1280.jpg"]

photos = dict(zip(random_photos, ['1', '2', '3']))


async def on_startup(_):
    print("Bot is executing")


@dp.message_handler(Text(equals="Random photo"))
async def open_kb_photo(message: types.Message):
    await message.answer(text="To get a random picture - press on a button called 'Random'.",
                         reply_markup=kb_photo)
    await message.delete()


@dp.message_handler(Text(equals="Random"))
async def send_random_photo(message: types.Message):
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo])


@dp.message_handler(Text(equals="Main menu"))
async def open_kb_photo(message: types.Message):
    await message.answer(text="Welcome back to main menu.",
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text="Welcome to our bot! 🐝",
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=HELP_TEXT,
                         parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def cmd_help(message: types.Message):
    await bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAEJbvJklASnB"
                                                    "ym5mF2sbsg-GzQRpT5FlwACdwADhIUKFrFQQrqaZrbXLwQ")
    await message.answer(text="Our bot has a lot of functions, discover them!")
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
