from aiogram import types, Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text

from keyboards import kb
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


async def on_startup(_):
    print("Bot is executing")


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
