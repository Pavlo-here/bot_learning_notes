from aiogram import types, executor, Dispatcher, Bot
from config import TOKEN_API
import random
import string

HELP_COMMAND = """
/help - cписок команд
/start - почати роботу з ботом
/description - отримати опис боту
/count - команда яка виводить кількість своїх виконань
"""
COUNT = 0

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])  # команда допомоги - виводить список доступних команд
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['start'])  # команда початку роботи з привітанням
async def hello_command(message: types.Message):
    await message.answer(text="Ласкаво просимо в наш телеграм бот!")
    await message.delete()


@dp.message_handler(commands=['description'])  # команда опису боту
async def description_command(message: types.Message):
    await message.answer(text="Цей бот створений для нових знайомств та організації подій.")
    await message.delete()


@dp.message_handler(commands=['count'])  # команда /count яка виводить кількість своїх виконань
async def count_command(message: types.Message):
    global COUNT
    await message.reply(text=str(COUNT))
    COUNT += 1


@dp.message_handler()  # чи є 0 в повідомленні користувача
async def zero_in_message(message: types.Message):
    if '0' in message.text:
        await message.reply(text="YES")
    else:
        await message.reply(text="NO")


@dp.message_handler()  # відповідь на будь-яке повідомлення випадковою літерою
async def rand_answer(message: types.Message):
    await message.answer(text=random.choice(string.ascii_letters))


if __name__ == "__main__":
    executor.start_polling(dp)
