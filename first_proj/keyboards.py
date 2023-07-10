from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text="/help"),
       KeyboardButton(text="/description"),
       KeyboardButton(text="/close"),
       KeyboardButton(text="Random photo"))

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
kb_photo.add(KeyboardButton(text="Random"), KeyboardButton(text="Main menu"))

ikb = InlineKeyboardMarkup(row_width=2)
ikb.add(InlineKeyboardButton(text='❤️', callback_data='like'),
        InlineKeyboardButton(text='👎', callback_data='dislike')) \
    .add(InlineKeyboardButton(text='Next photo', callback_data='next'))
