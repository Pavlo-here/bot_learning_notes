from aiogram import Dispatcher, types, Bot, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN_API
from lesson10_InlineKeyboard_module import ikb

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb.add(KeyboardButton(text="/help"), KeyboardButton(text="/start"))
kb.insert(KeyboardButton(text="/links"))


async def on_startup(_):
    print("Я запустився")


@dp.message_handler(commands=["start"])
async def start_func(message: types.Message):
    await bot.send_message(message.chat.id, text="Бот почав роботу", reply_markup=kb)


@dp.message_handler(commands=["links"])
async def start_func(message: types.Message):
    await bot.send_message(message.chat.id, text="Вітаємо у розділі посилань", reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
