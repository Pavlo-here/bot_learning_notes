from aiogram import types, Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
import random

from keyboards import kb, ikb
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

photos = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8"
          "/Altja_j%C3%B5gi_Lahemaal.jpg/1200px-Altja_j%C3%B5gi_Lahemaal.jpg",
          "https://natureconservancy-h.assetsadobe.com/is/image/content/dam/tnc/nature"
          "/en/photos/Zugpsitze_mountain.jpg?crop=0%2C214%2C3008%2C1579&wid=1200&hei=630&scl=2.506666666666667",
          "https://cdn.pixabay.com/photo/2014/02/27/16/10/flowers-276014_1280.jpg"]

photos_with_description = dict(zip(photos, ['River', 'Lake', 'Grass']))
random_photo = random.choice(list(photos_with_description.keys()))

flag = False


async def on_startup(_):
    print("Bot is executing")


async def get_rand_photo(message: types.Message):
    global random_photo  # небажано використовувати глобальні змінні
    random_photo = random.choice(list(photos_with_description.keys()))
    await bot.send_photo(message.chat.id,
                         photo=random_photo,
                         caption=photos_with_description[random_photo],
                         reply_markup=ikb)


@dp.message_handler(Text(equals="Random photo"))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Here is random photo',
                         reply_markup=ReplyKeyboardRemove())
    await get_rand_photo(message)
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


@dp.message_handler(commands=['location'])
async def cmd_location(message: types.Message):
    await bot.send_location(message.chat.id,
                            latitude=random.randint(0, 100),
                            longitude=random.randint(0, 100))


@dp.message_handler(commands=['close'])
async def close_func(message: types.Message):
    await bot.send_message(message.chat.id,
                           text='Keyboard closed.',
                           reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    global random_photo, flag  # небажано використовувати глобальні змінні
    if callback.data == 'like':
        if not flag:
            await callback.answer("You liked it!")
            flag = not flag
        else:
            await callback.answer("You've already liked it!")

    elif callback.data == 'dislike':
        await callback.answer("You disliked it")

    elif callback.data == 'menu':
        await callback.message.answer("Returned to main menu!", reply_markup=kb)
        await callback.message.delete()
        await callback.answer()

    elif callback.data == 'next':
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos_with_description.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type='photo',
                                                           caption=photos_with_description[random_photo]),
                                          reply_markup=ikb)
        await callback.answer()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
