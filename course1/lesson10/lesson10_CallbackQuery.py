# callback objects
from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я запустився')


kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text="/help"), KeyboardButton(text="/vote"))


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id,
                           text='Welcome to our bot!',
                           reply_markup=kb)


@dp.message_handler(commands=["vote"])
async def vote_func(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.add(InlineKeyboardButton(text='❤️', callback_data="like"),
            InlineKeyboardButton(text='👎', callback_data="dislike"))

    await bot.send_photo(message.from_user.id,
                         photo='https://i.natgeofe.com/n/fb80fae8-d096-4f5a-98ab-ec43830aa023/'
                               '20846.jpg?w=1084.125&h=813.75',
                         caption='Do you like our photo?',
                         reply_markup=ikb)


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == "like":
        await callback.answer(text="You've liked this photo!")
    if callback.data == "dislike":
        await callback.answer(text="You've disliked this photo!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
