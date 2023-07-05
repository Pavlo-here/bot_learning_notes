from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
/help
"""

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤️', url="google.com")
ib2 = InlineKeyboardButton(text='Inst', url="https://www.instagram.com/pasha.waves/")
ikb.add(ib1, ib2)


@dp.message_handler(commands=["start"])
async def help_func(message: types.Message):
    await bot.send_message(message.chat.id, text="Starting bot...",
                           reply_markup=ikb)


@dp.message_handler(commands=["help"])
async def help_func(message: types.Message):
    await bot.send_message(message.chat.id, text=HELP_COMMAND, parse_mode="HTML")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
