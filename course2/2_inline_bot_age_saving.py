import sys

sys.path.append("..")
from config import TOKEN_API_INLINE

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent


import hashlib


bot = Bot(token=TOKEN_API_INLINE)
dp = Dispatcher(bot)

user_age_data = ""


@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message) -> None:
    await message.answer(text="Input the number...")


@dp.message_handler()
async def text_handler(message: types.Message) -> None:
    global user_age_data
    user_age_data = message.text
    await message.reply(text="Ur data are saved")


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or "Echo"
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(
        f"<b>{text}</b> - {user_age_data}", parse_mode="html"
    )

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title="Echo bot!",
        description="Hi I'm not usual echo bot ^)",
    )

    await bot.answer_inline_query(
        results=[item],
        inline_query_id=inline_query.id,
        cache_time=1,
    )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
