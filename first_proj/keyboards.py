from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text="/help"),
       KeyboardButton(text="/description"),
       KeyboardButton(text="/close"),
       KeyboardButton(text="Random photo"))

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
kb_photo.add(KeyboardButton(text="Random"), KeyboardButton(text="Main menu"))
