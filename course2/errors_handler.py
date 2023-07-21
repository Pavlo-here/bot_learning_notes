import sys

sys.path.append("..")
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from config import TOKEN_API


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await asyncio.sleep(10)
    await message.answer("something")


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked_error(update: types.Update, exception: BotBlocked) -> bool:
    print("Can't send the message because we are blocked!")
    return True



if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
