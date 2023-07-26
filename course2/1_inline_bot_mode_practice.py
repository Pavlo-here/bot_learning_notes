import sys

sys.path.append("..")
from config import TOKEN_API_INLINE

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent


import hashlib


bot = Bot(token=TOKEN_API_INLINE)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message) -> None:
    await message.answer(text="Welcome to out bot!")


#  inlineQuery handlers
@dp.inline_handler()  #  process inlineQuery is formed by Telegram API
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or "Echo"  # got text from user
    result_id = hashlib.md5(text.encode()).hexdigest()  # created unique id

    if text == "photo":
        input_content = InputTextMessageContent("This is a photo!")
    else:
        input_content = InputTextMessageContent(text)

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title=text,
    )

    await bot.answer_inline_query(
        inline_query_id=inline_query.id,
        results=[item],
        cache_time=1,
    )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
