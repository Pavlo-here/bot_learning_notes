from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb = InlineKeyboardMarkup(row_width=2)
ikb.add(InlineKeyboardButton(text="Inst", url="https://www.instagram.com"),
        InlineKeyboardButton(text="Twitter", url="https://www.twitter.com"))
ikb.insert(InlineKeyboardButton(text="YT", url="https://www.youtube.com"))
