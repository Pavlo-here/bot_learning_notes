# sending location and photo
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/start</b> - <em>початок роботи</em>
<b>/help</b> - <em>інформація</em>
<b>/photo</b> - <em>показати зображення</em>
"""


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    #  await message.answer(message.text)
    #  await bot.send_message(chat_id=message.chat.id, text="Hello!")
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=["photo"])
async def send_img(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://i.guim.co.uk/img/media/453859dd4030b16164655cf89bd2d54b09e6c428/9_234_1049_630/"
                               "master/1049.jpg?width=620&quality=45&dpr=2&s=none")
    await message.delete()


@dp.message_handler(commands=["location"])
async def find_loc(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=55, longitude=55)
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
