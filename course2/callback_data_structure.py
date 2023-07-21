"""Exploring of CallbackData structure"""
import sys

sys.path.append("..")
from aiogram.utils.callback_data import CallbackData
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

cb = CallbackData("ikb", "action")


ikb = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton("Button", callback_data=cb.new("push"))]]
)


@dp.callback_query_handler(cb.filter())
async def ikb_callback_handler(
    callback: types.CallbackQuery, callback_data: dict
) -> None:
    if callback_data["action"] == "push":
        await callback.answer("Something")


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await message.answer(text="Hi!", reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
