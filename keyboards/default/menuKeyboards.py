from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Talim'),
            KeyboardButton(text='Freelancer'),
            KeyboardButton(text="O'quv kurslari"),
        ],
    ],
    resize_keyboard=True
)


agree = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ha'),
            KeyboardButton(text="Yo'q"),
        ],
    ],
    resize_keyboard=True
)
