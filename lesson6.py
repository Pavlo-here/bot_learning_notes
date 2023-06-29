from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> <em>- допомога зі списком команд чату</em>
<b>/give</b> <em>- подивитися цікавий стікер</em>
"""


async def on_startup(_):
    print('Бот почав свою роботу')


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.answer(HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=["give"])
async def give_command(message: types.Message):
    await message.answer("Дивись який смішний стікер ❤️")
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEJbvJklASnBym5mF2sbsg-GzQRpT5FlwACdwADhIUKFrFQQrqaZrbXLwQ")


@dp.message_handler()
async def send_black_heart(message: types.Message):
    if message.text == '❤️':
        await message.reply('🖤')
    if '✅' in message.text:
        await message.reply(str(message.text.count('✅')))


@dp.message_handler(content_types=["sticker"])
async def get_sticker_id(message: types.Message):
    await message.reply(message.sticker.file_id)
    await bot.send_sticker(message.from_user.id, sticker=message.sticker.file_id)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
