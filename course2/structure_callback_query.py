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
        ]
    ]
)


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://images.pexels.com/photos/147411/italy-mountains-dawn-daybreak-147411.jpeg?cs=srgb&dl=pexels-pixabay-147411.jpg&fm=jpg",
        caption="Do yo like this photo",
        reply_markup=ikb,
    )


@dp.callback_query_handler()
async def ikb_handler(callback: types.CallbackQuery):
    if callback.data == "like":
        await callback.answer(text="You liked thos photo!")
    else:
        await callback.answer(text="You disliked this photo!")





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
