from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот почав свою роботу')
    #  bot.send_message('Бот почав свою роботу')


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer('<em>Вітаю <b>вас</b> у нашому боті!</em>', parse_mode="HTML")


@dp.message_handler(commands=["give"])
async def give_command(message: types.Message):
    await message.delete()
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJbvJklASnBym5mF2sbsg-GzQRpT5FlwACdwADhIUKFrFQQrqaZrbXLwQ")


@dp.message_handler()
async def reply_with_emoji(message: types.Message):
    await message.reply(message.text + '❤️')


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
