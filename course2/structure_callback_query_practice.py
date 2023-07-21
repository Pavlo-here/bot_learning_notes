import sys

sys.path.append("..")
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("👍", callback_data="like"),
            InlineKeyboardButton("👎", callback_data="dislike"),
        ],
        [InlineKeyboardButton("Close", callback_data="close")],
    ]
)

marker = 0

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://media.macphun.com/img/uploads/macphun/blog/2063/_1.jpeg?q=75&w=1710&h=906&resize=cover",
        caption="Do yo like this photo",
        reply_markup=ikb,
    )


@dp.callback_query_handler()
async def photo_callback(callback: types.CallbackQuery):
    global marker
    if callback.data == "like" and marker != 1:
        await callback.answer(text="Liked it!")
        marker = 1
    elif callback.data == "dislike" and marker != 2:
        await callback.answer(text="Disliked it!")
        marker = 2
    elif callback.data == "close":
        await callback.message.delete()
    else:
        await callback.answer(text="Action already done!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
