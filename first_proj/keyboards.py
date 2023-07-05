from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text="/help"),
       KeyboardButton(text="/description"),
       KeyboardButton(text="/close"),
       KeyboardButton(text="Random photo"))
