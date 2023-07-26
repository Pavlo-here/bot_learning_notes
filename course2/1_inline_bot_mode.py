import sys

sys.path.append("..")
from config import TOKEN_API_INLINE

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent  # new imports for INLINE MODE!

import hashlib 


bot = Bot(token=TOKEN_API_INLINE)
dp = Dispatcher(bot)

cb = CallbackData("ikb", "action")


def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Button1", callback_data=cb.new("push1"))],
            [InlineKeyboardButton("Button2", callback_data=cb.new("push2"))],
        ]
    )

    return ikb


@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message) -> None:
    await message.answer(text="Welcome to out bot!", reply_markup=get_ikb())


@dp.callback_query_handler(cb.filter(action="push1"))
async def action_push1(callback: types.CallbackQuery) -> None:
    await callback.answer("Hello")


@dp.callback_query_handler(cb.filter(action="push2"))
async def action_push2(callback: types.CallbackQuery) -> None:
    await callback.answer("World!")


#  inlineQuery handlers
@dp.inline_handler()  #  process inlineQuery is formed by Telegram API
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or "Echo"  # got text from user
    input_content = InputTextMessageContent(text)  # creating answering content for user
    result_id = hashlib.md5(text.encode()).hexdigest()  # created unique id

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title="Echo ur's message.",
    )

    await bot.answer_inline_query(
        inline_query_id=inline_query.id,
        results=[item],
        cache_time=1,
    )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
