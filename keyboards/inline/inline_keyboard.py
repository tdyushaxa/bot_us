from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callbackData import talim_callback

talim = InlineKeyboardMarkup(row_width=2)
frelencer = InlineKeyboardMarkup(row_width=2)
data = {
    'ustoz': 'ustoz kerak',
    'sherik': 'sherik kerak',
    'job': 'ish joyi kerak',
    'xodim': 'xodim kerak',
    'shogird': 'shogird kerak'
}
for key, value in data.items():
    talim.insert(InlineKeyboardButton(text=value.capitalize(), callback_data=talim_callback.new(item__name=key)))

for key, value in data.items():
    frelencer.insert(InlineKeyboardButton(text=value.capitalize(), callback_data=talim_callback.new(item__name=key)))