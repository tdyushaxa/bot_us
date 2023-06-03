from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Talim'),
            KeyboardButton(text='Freelancer'),
        ],
    ],
    resize_keyboard=True
)
